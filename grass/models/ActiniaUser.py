###############################################################################
# Filename: ActiniaUser.py                                                     #
# Project: OpenPlains Inc.                                                     #
# File Created: Monday June 6th 2022                                           #
# Author: Corey White (smortopahri@gmail.com)                                  #
# Maintainer: Corey White                                                      #
# -----                                                                        #
# Last Modified: Thu Mar 07 2024                                               #
# Modified By: Corey White                                                     #
# -----                                                                        #
# License: GPLv3                                                               #
#                                                                              #
# Copyright (c) 2023 OpenPlains Inc.                                           #
#                                                                              #
# django-actinia is an open-source django app that allows for with             #
# the Actinia REST API for GRASS GIS for distributed computational tasks.      #
#                                                                              #
# This program is free software: you can redistribute it and/or modify         #
# it under the terms of the GNU General Public License as published by         #
# the Free Software Foundation, .either version 3 of the License, or           #
# (at your option) any later version.                                          #
#                                                                              #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU General Public License for more details.                                 #
#                                                                              #
# You should have received a copy of the GNU General Public License            #
# along with this program.  If not, see <https://www.gnu.org/licenses/>.       #
#                                                                              #
###############################################################################

# import os
from typing import Any
from django.db import models

# from django.contrib.auth.models import BaseUserManager
from django.utils.crypto import get_random_string
from .ObjectAuditAbstract import ObjectAuditAbstract
from .fields.ActiniaRoleEnumField import ActiniaRoleEnumField

# from .enums import RolesEnum
from django.conf import settings

# from actinia import Actinia
# from requests.auth import HTTPBasicAuth
# from enum import Enum, unique
# from .Location import Location
# from .Mapset import Mapset
# from .Token import Token
from grass.services import ActiniaUserService

ACTINIA_SETTINGS = settings.ACTINIA


class ActiniaUserManager(models.Manager):
    """
    Manager class for ActiniaUser model.

    This manager provides methods for creating and deleting ActiniaUser objects.

    Attributes:
        actinia_user_service (ActiniaUserService): An instance of the ActiniaUserService class.

    """

    actinia_user_service = ActiniaUserService()

    def create_actinia_user(self, user, actinia_role, epsg=3358):
        """
        Create a new actinia user.

        Args:
            user (User): The Django user object.
            actinia_role (str): The role of the actinia user.
            epsg (int): The EPSG code to use for the default location.

        Returns:
            ActiniaUser: The new actinia user.

        """

        actinia_username = user.username
        actinia_role = actinia_role
        password = get_random_string(23)

        actinia_user = self.actinia_user_service.create_actinia_user(
            user=user, group=actinia_role, user_id=actinia_username, password=password
        )

        return actinia_user

    def delete_actinia_user(self, actinia_user):
        """
        Delete an actinia user.

        Args:
            actinia_user (ActiniaUser): The actinia user to delete.

        """

        self.actinia_user_service.delete_actinia_user(actinia_user)


class ActiniaUser(ObjectAuditAbstract):
    """
    Custom user class to manage actinia user.

    Attributes:
        actinia_username (str): The username of the actinia user.
        actinia_role (ActiniaRoleEnumField): The role of the actinia user.
        user (ForeignKey): The related Django user object.
        password (str): The password of the actinia user.
    """

    actinia_username = models.CharField(max_length=50, blank=False, unique=True)
    actinia_role = ActiniaRoleEnumField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="actinia_users", on_delete=models.CASCADE
    )
    password = models.CharField(max_length=128)
    objects = ActiniaUserManager()

    def save(self, *args, **kwargs):
        """
        Save an actinia user. This could mean creating a new user or updating an existing one.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Make a DELETE request to the other API
        try:
            ActiniaUser.objects.delete_actinia_user(self)
        except Exception as e:
            print("Error deleting actinia user: ", e)
        # Call the superclass's delete method to delete the ActiniaUser instance
        super().delete(*args, **kwargs)

    def __str__(self):
        """
        Return the actinia username.

        Returns:
            str: The actinia username.
        """
        return self.actinia_username

    class Meta:
        """
        Metadata for the ActiniaUser model.
        """

        ordering = ["created_on"]
        verbose_name = "Actinia User"
        verbose_name_plural = "Actinia Users"
        db_table = "actinia_users"
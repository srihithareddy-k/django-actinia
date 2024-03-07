###############################################################################
# Filename: test_ActiniaUserService.py                                         #
# Project: OpenPlains Inc.                                                     #
# File Created: Friday November 17th 2023                                      #
# Author: Corey White (smortopahri@gmail.com)                                  #
# Maintainer: Corey White                                                      #
# -----                                                                        #
# Last Modified: Wed Mar 06 2024                                               #
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
# the Free Software Foundation, either version 3 of the License, or            #
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


# from django.test import TestCase
# from django.http import JsonResponse
# from actinia_openapi_python_client import ApiException
# from grass.models import ActiniaUser
# from grass.services.ActiniaUserService import ActiniaUserService
# from django.contrib.auth.models import User


# class TestActiniaUserService(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # cls.actinia_user_service = ActiniaUserService()
#         # Set up non-modified objects used by all test methods
#         cls.user = User.objects.create_user(
#             username="test_user_id", email="testuser@example.com", password="testpass"
#         )
#         cls.actinia_user = ActiniaUser.create_actinia_user(cls.user, "admin")

#     def setUp(self):
#         self.actinia_user_service = ActiniaUserService()

#     def test_create_actinia_user_already_exists(self):
#         with self.assertRaises(Exception):
#             # Test the create_actinia_user method
#             user = self.user
#             user_id = "test_user_id"
#             password = "test_password"
#             group = "admin"
#             self.actinia_user_service.create_actinia_user(
#                 user, user_id, password, group
#             )

#     def test_get_actinia_users(self):
#         # Test the get_actinia_users method
#         response = self.actinia_user_service.get_actinia_users()
#         self.assertIsInstance(response, JsonResponse)

#     def test_get_actinia_user(self):
#         # Test the get_actinia_user method
#         user_id = "test_user_id"
#         response = self.actinia_user_service.get_actinia_user(user_id)
#         self.assertIsInstance(response, JsonResponse)

#     def test_delete_actinia_user(self):
#         # Test the delete_actinia_user method
#         response = self.actinia_user_service.delete_actinia_user(self.actinia_user)
#         self.assertIsInstance(response, JsonResponse)
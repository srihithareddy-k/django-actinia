###############################################################################
# Filename: locations.py                                                       #
# Project: OpenPlains                                                          #
# File Created: Monday June 6th 2022                                           #
# Author: Corey White (smortopahri@gmail.com)                                  #
# Maintainer: Corey White                                                      #
# -----                                                                        #
# Last Modified: Tue Jun 07 2022                                               #
# Modified By: Corey White                                                     #
# -----                                                                        #
# License: GPLv3                                                               #
#                                                                              #
# Copyright (c) 2022 OpenPlains                                                #
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

import requests
import actinia.utils as acp
from django.http import JsonResponse


def gLocations(request):
    """
    Gets List of Users Avaliable Locations
    Actinia Route
    GET /locations
    """
    if request.method == "GET":
        url = f"{acp.baseUrl()}/locations"
        r = requests.get(url, auth=acp.auth())
        print(f"Request URL: {url}")
        return JsonResponse({"response": r.json()}, safe=False)

    # TODO - Set up proper error handling and reponse messages
    return JsonResponse({"error": "gLocations View: Fix Me"})

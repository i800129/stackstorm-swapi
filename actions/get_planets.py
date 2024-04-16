


# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
'''

░██████╗████████╗░█████╗░██████╗░░██╗░░░░░░░██╗░█████╗░██████╗░░██████╗  ░█████╗░██████╗░██╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗░██║░░██╗░░██║██╔══██╗██╔══██╗██╔════╝  ██╔══██╗██╔══██╗██║
╚█████╗░░░░██║░░░███████║██████╔╝░╚██╗████╗██╔╝███████║██████╔╝╚█████╗░  ███████║██████╔╝██║
░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░████╔═████║░██╔══██║██╔══██╗░╚═══██╗  ██╔══██║██╔═══╝░██║
██████╔╝░░░██║░░░██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║██████╔╝  ██║░░██║██║░░░░░██║
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  ╚═╝░░╚═╝╚═╝░░░░░╚═╝
'''
#------------------------------------------------------------------------------#
#                                                                              #
# __author__ = "@netwookie"                                                    #
# __credits__ = ["Rick Kauffman"]                                              #
# __license__ = "Apache2.0"                                                    #
# __maintainer__ = "Rick Kauffman"                                             #
# __email__ = "rick#rickkauffman.com"                                          #
#                                                                              #
#                                                                              #
#------------------------------------------------------------------------------#
import urllib3
import requests
import json
from utility.get_urls import get_urls
from lib.actions import SwapiBaseAction
urllib3.disable_warnings()

__all__ = [
    'Planets'
]


class Planets(SwapiBaseAction):
    def run(self):
        list_of_planets = []
        url = self.baseurl+'/planets/'
        urls = get_urls(url)
        for item in urls:
            response = requests.get(item)
            json_data = json.loads(response.content)
            info = [
                    json_data['name'],
                    json_data['rotation_period'],
                    json_data['orbital_period'],
                    json_data['diameter'],
                    json_data['climate'],
                    json_data['gravity'],
                    json_data['terrain'],
                    json_data['surface_water'],
                    json_data['population'],
                    json_data['residents'],
                    json_data['films'],
                    json_data['url']
                    ]
            list_of_planets.append(info)
            info = []
        return list_of_planets

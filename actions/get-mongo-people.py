

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0.

# Unless required by applicable law. or agreed to in writing, software
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
from lib.actions import MongoBaseAction
import json

__all__ = [
    'GetDb'
]


class GetDb(MongoBaseAction):
    def run(self):

        mydb = self.dbclient["swapi"]
        known = mydb["people"]

        list_to_process = []
        person = {}

        myquery = {"u_process": 'no'}
        people = list(known.find(myquery))

        for item in people:
            person['u_name'] = item['u_name']
            person['u_height'] = item['u_height']
            person['u_mass'] = item['u_mass']
            person['u_haircolor'] = item['u_haircolor']
            person['u_skincolor'] = item['u_skincolor']
            person['u_eyecolor'] = item['u_eyecolor']
            person['u_birthyear'] = item['u_birthyear']
            person['u_gender'] = item['u_gender']
            person['u_homeworld'] = item['u_homeworld']
            person['u_films'] = item['u_films']
            person['u_species'] = item['u_species']
            person['u_vehicles'] = item['u_vehicles']
            person['u_starships'] = item['u_starships']
            person['u_snowprocess'] = 'no'
            person['u_kafkaprocess'] = 'no'
            list_to_process.append(person)
            person= {}

        return (list_to_process)

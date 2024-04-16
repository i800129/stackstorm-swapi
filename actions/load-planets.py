

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

__all__ = [
    'LoadDb'
]


class LoadDb(MongoBaseAction):
    def run(self, planets):

        db = self.dbclient["swapi"]

        planet = {}

        for item in planets:
            message = 'processing people'
            if db.planets.count_documents({ 'u_name': item[0] }, limit = 1) == 0:
                planet['u_name'] = item[0]
                planet['u_rotation_period'] = item[1]
                planet['u_orbital_period'] = item[2]
                planet['u_diameter'] = item[3]
                planet['u_climate'] = item[4]
                planet['u_gravity'] = item[5]
                planet['u_terrain'] = item[6]
                planet['u_surface_water'] = item[7]
                planet['u_population'] = item[8]
                planet['u_residents'] = item[9]
                planet['u_films'] = item[10]
                planet['u_created'] = item[11]
                planet['u_edited'] = item[12]
                planet['u_url'] = item[13]
                planet['u_snowprocess'] = 'no'
                planet['u_kafkaprocess'] = 'no'
                write_record = db.planets.insert_one(planet)
                planet= {}

            else:
                message = 'Fail to write mongo record, possible duplicate'
                # write_record = process.insert_one(alarm)
        return (message)

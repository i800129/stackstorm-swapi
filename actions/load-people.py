

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
    def run(self, people):

        db = self.dbclient["swapi"]

        person = {}

        for item in people:
            message = 'processing people'
            if db.people.count_documents({ 'u_name': item[0] }, limit = 1) == 0:
                person['u_name'] = item[0]
                person['u_height'] = item[1]
                person['u_mass'] = item[2]
                person['u_haircolor'] = item[3]
                person['u_skincolor'] = item[4]
                person['u_eyecolor'] = item[5]
                person['u_birthyear'] = item[6]
                person['u_gender'] = item[7]
                person['u_homeworld'] = item[8]
                person['u_films'] = item[9]
                person['u_species'] = item[10]
                person['u_vehicles'] = item[11]
                person['u_starships'] = item[12]
                person['u_snowprocess'] = 'no'
                person['u_kafkaprocess'] = 'no'
                write_record = db.people.insert_one(person)
                person= {}

            else:
                message = 'Fail to write mongo record, possible duplicate'
                # write_record = process.insert_one(alarm)
        return (message)


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

def get_urls(resource):
''' Get all the URLs for every resource'''
    urls = []
    next = True
    while next:
        response = requests.get(query)
        json_data = json.loads(response.content)
        for resource in json_data['results']:
            urls.append(resource['url'])
        if bool(json_data['next']):
            resource = json_data['next']
        else:
            next = False
        return(urls)

import json
import requests
import swapi
from utility.get_urls import get_urls
baseurl = 'https://swapi.dev/api'

query = baseurl+'/people/'

print(query)

#people = swapi.get_person(1)
#print(people)
count = 0
#response = requests.get('https://swapi.dev/api/people/78/')
#json_data = json.loads(response.content)
#print(json_data['name'])

urls = get_urls(query)
print('len of urls'+str(len(urls)))

for item in urls:
    count = count + 1
    response = requests.get(item)
    json_data = json.loads(response.content)
    print(json_data['name'])
    line = str(count) + '++++++++++++++++++++++++++++++++++++++'
    print(line)

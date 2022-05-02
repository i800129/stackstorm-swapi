import json
import requests
import swapi
baseurl = 'http://swapi.dev/api'

query = baseurl+'/people/'

print(query)

#people = swapi.get_person(1)
#print(people)
count = 0
#response = requests.get('https://swapi.dev/api/people/78/')
#json_data = json.loads(response.content)
#print(json_data['name'])

''' Get all the URLs for every resource'''
urls = []
next = True
while next:
    response = requests.get(query)
    json_data = json.loads(response.content)
    for resource in json_data['results']:
        urls.append(resource['url'])
    if bool(json_data['next']):
        query = json_data['next']
    else:
        next = False
print('len of urls'+str(len(urls)))
for item in urls:
    count = count + 1
    response = requests.get(item)
    json_data = json.loads(response.content)
    print(json_data)
    line = str(count) + '++++++++++++++++++++++++++++++++++++++'
    print(line)

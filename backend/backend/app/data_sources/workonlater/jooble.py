#USA BASED

import requests
import pprint

host = 'https://jooble.org' 
key = '97ba3a3a-21ab-445f-a49b-f220871f0c63'

url = f"{host}/api/{key}"

headers = {"Content-type": "application/json"}
data = {
    # doesnt have certain keywords
    "keywords": "front-end, software, remote, junior",
    "location": "India",
    # "radius": "25",
    "page": "1",
}
response = requests.post(url, json=data, headers=headers)
response = response.json()

# length = (response['totalCount'])

pprint.pprint(response)
# print(f'Number of jobs found: {length}')


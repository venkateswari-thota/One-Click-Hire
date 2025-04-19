import requests

id = '54'
url = f'https://www.bctechjobs.ca/api/v1.1/jobs/{id}'

def bcTech():
    html = requests.get(url)
    data = html.json()
    print(data)

bcTech()
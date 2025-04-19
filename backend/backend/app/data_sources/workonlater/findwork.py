import requests

url = 'https://findwork.dev/api/jobs/?search=javascript&source=&location=canada&remote=true&company_num_employees=&employment_type=&order_by=date'
html = requests.get(url)

data = html.json()
print(data)
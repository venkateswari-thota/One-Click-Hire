# import requests
# from dotenv import load_dotenv
# import os
# load_dotenv()

# def adzuna(title, location):
#     try:

#         pageNumber = 1
#         country = 'in'
#         title = title.replace(' ', '%20')

#         url = f'http://api.adzuna.com/v1/api/jobs/{country}/search/{pageNumber}?app_id={os.getenv("ADZUNA_ID")}&app_key={os.getenv("ADZUNA_API_KEY")}&where={location}&what={title}&sort_by=relevance&results_per_page=10&content-type=application/json'
#         html = requests.get(url)
        
#         data = html.json()
        
#         data = data['results']
        
#         jobs = []

#         for job in data:
#             obj = {
#                 'title': job['title'],
#                 'company': job['company']['display_name'],
#                 'location': job['location']['display_name'],
#                 'url': job['redirect_url'],
#                 'description': job['description']
#             }
#             jobs.append(obj)
        
#         return jobs
    
#     except Exception as error:
#         print("An error occurred:", error)




import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def adzuna(title, location):
    try:
        pageNumber = 1
        country = 'in'
        title = title.replace(' ', '%20')

        # Get API credentials
        adzuna_id = os.getenv("ADZUNA_ID")
        adzuna_api_key = os.getenv("ADZUNA_API_KEY")

        if not adzuna_id or not adzuna_api_key:
            print("Error: Missing Adzuna API credentials.")
            return []

        # API request URL
        url = f'http://api.adzuna.com/v1/api/jobs/{country}/search/{pageNumber}?app_id={adzuna_id}&app_key={adzuna_api_key}&where={location}&what={title}&sort_by=relevance&results_per_page=10&content-type=application/json'
        #print(f"Fetching jobs from Adzuna API: {url}")  # Debugging line

        response = requests.get(url)
        
        # Check if API request was successful
        if response.status_code != 200:
            print(f"Adzuna API request failed: {response.status_code}, {response.text}")
            return []

        data = response.json()

        # Ensure 'results' key exists
        if 'results' not in data:
            print("Error: Unexpected Adzuna response format", data)
            return []

        jobs = []
        for job in data['results']:
            obj = {
                'title': job.get('title', 'N/A'),
                'company': job.get('company', {}).get('display_name', 'Unknown'),
                'location': job.get('location', {}).get('display_name', 'Unknown'),
                'url': job.get('redirect_url', ''),
                'description': job.get('description', 'No description available.')
            }
            jobs.append(obj)

        return jobs

    except Exception as error:
        print("An error occurred while fetching Adzuna jobs:", error)
        return []

# print(adzuna("Software Engineer", "Bangalore"))

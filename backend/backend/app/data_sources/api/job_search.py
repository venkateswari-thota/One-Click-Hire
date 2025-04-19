# import requests
# from dotenv import load_dotenv
# import os
# load_dotenv()

# def job_search(title, location):

#     url = "https://jobsearch-api2.p.rapidapi.com/api/v2/Jobs/Search"

#     querystring = {"SearchQuery":f'{title} {location}',"PageSize":"25","PageNumber":"1"}

#     headers = {
#         "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
#         "X-RapidAPI-Host": "job-search-api2.p.rapidapi.com"
#     }

#     response = requests.get(url, headers=headers, params=querystring)

#     data = response.json()
#     print("data",data)
#     data = data["data"]

#     jobs = []

#     for job in data:
#         dict = {
#             "title": job["title"],
#             "company": job["company"],
#             "location": '',
#             "url": job["url"],
#             "description": ''
#         }
#         jobs.append(dict)
        
#     return jobs


import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Load API key from .env

def job_search(title, location):
    url = "https://jsearch.p.rapidapi.com/estimated-salary?job_title=nodejs%20developer&location=new%20york&location_type=ANY&years_of_experience=ALL"
    
    querystring = {"SearchQuery": f"{title} {location}", "PageSize": "25", "PageNumber": "1"}

    headers = {
        "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code != 200:
        print(f"API request failed in job search! Status Code: {response.status_code}, Response: {response.text}")
        return []

    try:
        data = response.json()
        #print("Full API Response:", data)  # Debugging

        if "data" not in data:
            print("Error: 'data' key missing in response")
            return []

        data = data["data"]

    except Exception as e:
        print("Error processing API response:", e)
        return []

    jobs = []

    for job in data:
        jobs.append({
            "title": job.get("title", ""),
            "company": job.get("company", ""),
            "location": job.get("location", ""),  # Added location
            "url": job.get("url", ""),
            "description": job.get("description", "")  # Added description
        })
    jobs = [job for sublist in job_search(title, location) for job in sublist]

    return jobs

# Test call
# print(job_search("Software Engineer", ""))

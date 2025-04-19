# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()  # Load environment variables from .env file

# def findwork(title, location):
#     try:
#         api_key = os.getenv("FINDWORK_API_KEY")  # Get API key from environment variables
#         url = "https://findwork.dev/api/jobs/"

#         headers = {
#             "Authorization": f"Token {api_key}"
#         }

#         params = {
#             "search": f"{title} {location}",
#             "limit": 20  # Adjust limit as needed
#         }

#         response = requests.get(url, headers=headers, params=params)
#         response_data = response.json()

#         if "results" not in response_data:
#             print("Invalid response from Findwork API:", response_data)
#             return []

#         jobs = [
#             {
#                 "title": job["role"],
#                 "company": job["company_name"],
#                 "location": job["location"],
#                 "url": job["url"],
#                 "description": job["text"],
#             }
#             for job in response_data["results"]
#         ]

#         return jobs

#     except Exception as e:
#         print("Error fetching jobs from Findwork API:", str(e))
#         return []

# # Example usage:
# # jobs = fetch_findwork_jobs("Software Engineer", "Remote")
# # print(jobs)



import requests
import os
import re
import html
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def clean_html(text):
    """ Remove HTML tags and decode HTML entities """
    if not text:
        return ""
    
    text = html.unescape(text)  # Decode HTML entities like &gt;, &amp;
    text = re.sub(r"<.*?>", " ", text)  # Remove HTML tags
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces & newlines
    return text

def findwork(title, location):
    try:
        api_key = os.getenv("FINDWORK_API_KEY")  # Get API key from environment variables
        if not api_key:
            print("Error: FINDWORK_API_KEY is missing in .env")
            return []

        url = "https://findwork.dev/api/jobs/"
        headers = {"Authorization": f"Token {api_key}"}
        params = {"search": f"{title} {location}", "limit": 20}

        response = requests.get(url, headers=headers, params=params)

        # Check if the request was successful
        if response.status_code != 200:
            print(f"Error: Findwork API returned status {response.status_code}")
            print("Response:", response.text)
            return []

        response_data = response.json()

        # Check if the expected data exists
        if "results" not in response_data:
            print("Invalid response from Findwork API:", response_data)
            return []

        # Process jobs
        jobs = [
            {
                "title": job.get("role", "N/A"),
                "company": job.get("company_name", "Unknown"),
                "location": job.get("location", "Not Specified"),
                "url": job.get("url", ""),
                "description": clean_html(job.get("text", "")),  # CLEAN THE TEXT HERE
            }
            for job in response_data["results"]
        ]

        return jobs

    except Exception as e:
        print("Error fetching jobs from Findwork API:", str(e))
        return []

# Test the function
# if __name__ == "__main__":
#     jobs = findwork("Software Engineer", "Remote")
#     print(jobs)  # Debug output

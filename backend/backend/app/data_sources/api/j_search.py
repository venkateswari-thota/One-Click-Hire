import requests
from dotenv import load_dotenv
import os
import re
import html

load_dotenv()  # Load environment variables from .env file

def clean_html(text):
    """ Remove HTML tags and decode HTML entities """
    if not text:
        return ""
    
    text = html.unescape(text)  # Decode HTML entities (&gt;, &amp;)
    text = re.sub(r"<.*?>", " ", text)  # Remove HTML tags
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces & newlines
    return text

def j_search(title, location):
    url = "https://jsearch.p.rapidapi.com/search"
    querystring = {"query": f"{title} in {location}", "page": "1", "num_pages": "1"}

    headers = {
        "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        
        if response.status_code != 200:
            print(f"Error: JSearch API returned status {response.status_code}")
            print("Response:", response.text)
            return []

        data = response.json()
        if "data" not in data:
            print("Invalid response from JSearch API:", data)
            return []

        jobs = []
        for job in data["data"]:
            description = clean_html(job.get("job_description", "")).replace("\n", " ")

            # Shorten description to 500 characters
            if len(description) > 500:
                description = description[:500] + "..."

            job_entry = {
                "title": job.get("job_title", "N/A"),
                "company": job.get("employer_name", "Unknown"),
                "location": f'{job.get("job_city", "N/A")}, {job.get("job_country", "N/A")}',
                "url": job.get("job_apply_link", ""),
                "description": description
            }
            jobs.append(job_entry)

        return jobs

    except Exception as e:
        print("Error fetching jobs from JSearch API:", str(e))
        return []

# Example usage:
# if __name__ == "__main__":
#     results = j_search("Software Developer", "India")
#     for job in results:
#         print(job)

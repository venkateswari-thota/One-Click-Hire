import os
import requests
from dotenv import load_dotenv
import re
from bs4 import BeautifulSoup  # ✅ Use this for HTML cleanup

# Load environment variables from .env file
load_dotenv()

def clean_html(raw_html):
    """Removes HTML tags and decodes entities."""
    soup = BeautifulSoup(raw_html, "html.parser")
    return soup.get_text().replace("\r", "").replace("\n", " ").strip()

def jooble(title, location):
    try:
        api_key = os.getenv("JOOBLE_API_KEY")  # Get API key from .env
        url = f"https://jooble.org/api/{api_key}"

        payload = {
            "keywords": f"{title} {location}",
            "location": location,
            "page": 1
        }

        response = requests.post(url, json=payload)
        
        if response.status_code != 200:
            print(f"Jooble API error: {response.status_code} - {response.text}")
            return []

        response_data = response.json()

        if "jobs" not in response_data:
            print("Invalid response from Jooble API:", response_data)
            return []

        jobs = [
            {
                "title": job.get("title", "Unknown Title"),
                "company": job.get("company", "Unknown Company"),
                "location": job.get("location", "Unknown Location"),
                "url": job.get("link", ""),
                "description": clean_html(job.get("snippet", "")),  # ✅ Fix: Removes HTML
            }
            for job in response_data["jobs"]
        ]

        return jobs

    except Exception as e:
        print("Error fetching jobs from Jooble API:", str(e))
        return []

# Example usage:
# # if __name__ == "__main__":
#     results = jooble("Software Developer", "Remote")
#     for job in results:
#         print(job)

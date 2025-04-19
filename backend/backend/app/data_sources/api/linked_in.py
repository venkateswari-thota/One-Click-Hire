from linkedin_api import Linkedin
import os 
from dotenv import load_dotenv
load_dotenv()
import pprint

def linked_in(title, location):
# Authenticate using any Linkedin account credentials
    api = Linkedin(os.getenv("LINKEDIN_USERNAME"), os.getenv("LINKEDIN_PASSWORD"))

    data = api.search_jobs(remote=True, limit=25, keywords=title, experience=['1', '2', '3'], listed_at='691200', location_name=location)

    jobs = []

    for job in data:

        # Retrieve company id from job data
        companyString = job['companyDetails']['company']
        company = companyString.replace('urn:li:fsd_jobPosting:', '')

        # Retreive job id from job data
        idString = job['dashEntityUrn']
        id = idString.replace('urn:li:fsd_jobPosting:', '')
        url = f'http://www.linkedin.com/jobs/view/{id}'

        dict = {
            "title": job["title"],
            "company": f'http://www.linkedin.com/company/{company}',
            "location": job["formattedLocation"],
            "url": url,
            "description": ''
        }
        jobs.append(dict)

    return jobs

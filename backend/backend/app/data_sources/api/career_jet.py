# from careerjet_api_client import CareerjetAPIClient

# def career_jet(title, location):
 
#     cj  =  CareerjetAPIClient("en_IN")

#     result_json = cj.search({
#                             'location'    : location,
#                             'keywords'    : title,
#                             'sort'        : 'relevance',
#                             'pagesize'    : '25',
#                             'affid'       : '213e213hd12344552',
#                             'user_ip'     : '11.22.33.44',
#                             'url'         : 'http://www.example.com/jobsearch?q=python&l=london',
#                             'user_agent'  : 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
#                         })

#     data = result_json['jobs']

#     jobs = []

#     for job in data:
#         dict = {
#             'title': job['title'],
#             'company': job['company'],
#             'location': job['locations'],
#             'url': job['url'],
#             'description': job['description'],
#         }
#         jobs.append(dict)

#     return jobs



from careerjet_api_client import CareerjetAPIClient
from bs4 import BeautifulSoup

def career_jet(title, location):
    try:
        # Initialize CareerJet API Client for India
        cj = CareerjetAPIClient("en_IN")

        # API request parameters
        result_json = cj.search({
            'location': location,
            'keywords': title,
            'sort': 'relevance',
            'pagesize': 25,
            'affid': '213e213hd12344552',  # Affiliate ID
            'user_ip': '11.22.33.44',  # Use actual IP in production
            'url': f'http://www.example.com/jobsearch?q={title}&l={location}',
            'user_agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
        })

        # Debugging output
        #print(f"CareerJet API Response: {result_json}")

        # Ensure 'jobs' key exists in response
        if 'jobs' not in result_json:
            print("Error: Unexpected CareerJet response format", result_json)
            return []

        jobs = []
        for job in result_json['jobs']:
             # Clean the description from HTML tags
            raw_description = job.get('description', 'No description available.')
            clean_description = BeautifulSoup(raw_description, "html.parser").get_text()
            job_data = {
                'title': job.get('title', 'N/A'),
                'company': job.get('company', 'Unknown'),
                'location': job.get('locations', 'Unknown'),
                'url': job.get('url', ''),
                #'description': job.get('description', 'No description available.')
                'description': clean_description.strip()

            }
            jobs.append(job_data)

        return jobs

    except Exception as error:
        print("An error occurred while fetching CareerJet jobs:", error)
        return []

#print(career_jet("Software Engineer", "Bangalore"))

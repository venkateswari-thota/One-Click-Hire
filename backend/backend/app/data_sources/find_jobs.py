# from .api.adzuna import adzuna
# from .api.career_jet import career_jet
# from .api.findwork import findwork
# from .api.jooble import jooble



# def find_jobs(title, location):

#     # Collect job data from all APIs
#     alljobs = [
#         *adzuna(title, location),
#         *career_jet(title, location),
       
#         *findwork(title,location),
#         *jooble(title,location)

#     ]

   
#     return alljobs

# if __name__ == "__main__":
#     title = "Software Engineer"  # Sample input
#     location = "India"
    
#     jobs = find_jobs(title, location)
#     print("Final job results:", jobs)




# def find_jobs(title, location):
#     try:
#         jobs = []
#         jobs+=adzuna(title,location)
#         jobs+=career_jet(title,location)
#         jobs+=j_search(title,location)
#         jobs += jooble(title, location)  # Fix: Append jobs properly
#         jobs += findwork(title, location)  # Fix: No need for "*"
#         return jobs
#     except Exception as e:
#         print("Error fetching jobs:", e)
#         return []




from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
from .api.adzuna import adzuna
from .api.career_jet import career_jet
from .api.findwork import findwork
from .api.jooble import jooble

app = Flask(__name__)
CORS(app) 

def find_jobs(title, location):
    all_jobs = []
    for source, func in {
        "Adzuna": adzuna,
        "CareerJet": career_jet,
        "FindWork": findwork,
        "Jooble": jooble,
    }.items():
        try:
            jobs = func(title, location) or []
            all_jobs.extend(jobs)
        except Exception as e:
            print(f"❌ Error fetching jobs from {source}: {str(e)}")  
    return all_jobs

# @app.route("/jobs", methods=["GET"])
# def get_jobs():
#     title = request.args.get("title", "Software Engineer")
#     location = request.args.get("location", "India")
#     jobs = find_jobs(title, location)

#     return jsonify({"jobs": jobs})  # Returning JSON

# if __name__ == "__main__":
#     app.run(debug=True)


# #One-click hire
# import requests
# from config import GROQ_API_KEY

# # Groq API setup
# API_URL = "https://api.groq.com/openai/v1/chat/completions"
# HEADERS = {
#     "Authorization": f"Bearer {GROQ_API_KEY}",
#     "Content-Type": "application/json",
# }

# def get_model_response(query):
#     prompt = f"""
#     You are the job queries answering agent/chatbot named One-Click Hire Bot implemented by Team Missiles.
#     Implementors: T.Venkateswari (N200649), SK.Asiya Tabasum (N200170), and S.Lahari (N200171)-department of CSE(compuetr science and engineering)-3 
#     rd year of engineering in RGUKT - Nuzvid(Rajiv gandhi University Of Knowledge Technologies-Nuzvid).
#     Platform: One-Click Hire - Transform job applications with AI automation.

#     Features:
#     - Submit your resume or create yor resume.
#     - Job recommendations based on user skills and achievements from uplaoded resume.
#     - Filtering jobs based on location and interest(Location and job set by user).
#     - Resume creation, ATS score, resume enhancement.
#     - One-click job application after submitting a resume.
#     - Automatic form filling for job applications.
    

#     Rules:
#     1. If the query is about 'One-Click Hire,' answer based on the provided platform details.
#     2. If the query is about jobs (hiring process, resume, interview tips, etc.), use general LLM knowledge.
#     3.If the query is a **greeting** (e.g., "hi", "hello", "hey", "who are you?","who are you?","hola","namaskhar","aadab","i miss you","can you help me?","how can you help me"), give a **short and friendly** response like:  
#        **"Hello! This is One-Click Hire Bot. How can I assist you?
#     4. If the query is unrelated, reply with: "I couldn't get you! This query is out of my field.
#     User Query: {query}
#     Response:
#     """

#     payload = {
#         "model": "mixtral-8x7b-32768",
#         "messages": [
#             {"role": "system", "content": prompt},
#             {"role": "user", "content": query},
#         ],
#         "temperature": 0.7,
#     }
    
#     response = requests.post(API_URL, json=payload, headers=HEADERS)

#     if response.status_code == 200:
#         return response.json()["choices"][0]["message"]["content"]
#     else:
#         return f"Error: {response.status_code}, {response.text}"



#Ai security surveillance
import requests
from config import GROQ_API_KEY

# Groq API setup
API_URL = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json",
}

def get_model_response(query):
    prompt = f"""
    You are an AI Security Surveillance System Bot, designed to assist users with security-related inquiries.
    
    Implementors: 
    - T.Venkateswari (N200649) 
    - SK.Asiya Tabasum (N200170) 
    - S.Lahari (N200171)
    - Team missiles.
    - Department of CSE (Computer Science and Engineering)  
    - 3rd Year, RGUKT - Nuzvid (Rajiv Gandhi University of Knowledge Technologies, Nuzvid) 
     
    Platform: AI Security Surveillance System
    - Features:  
      - Harmful object detection  
      - Abnormal activity detection  
      - Tampering detection  
      - Alert generation for detected threats  

    Rules for Response Generation:
    1. If the user query is about security (e.g., video surveillance, AI security, crime prevention, home security, threat detection), provide an **accurate response**.  
    2. If the query is about our platform’s features, answer with details on harmful object detection, abnormal activity tracking, or tampering detection.  
    3. If the query is a greeting(e.g., "hi", "hello", "who are you?","how are you?","can you help me?","how can you help me?"), respond with:  
       "I am Security Bot! Here to assist you with security-related queries."  
    4. If the query is not related to security, reply with:  
       "I couldn't get you! The query is not related to security."

    User Query: {query}  
    Response:
    """

    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": query},
        ],
        "temperature": 0.7,
    }
    
    response = requests.post(API_URL, json=payload, headers=HEADERS)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"

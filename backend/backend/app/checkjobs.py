# import sys
# import os

# # Add the backend directory to Python path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from app import create_app, db
# from app.models import Job

# # Create a Flask app instance
# app = create_app()

# # Use application context
# with app.app_context():
#     jobs = Job.query.order_by(Job.created_at.desc()).all()
#     for job in jobs:
#         print(f"ID: {job.id}, Title: {job.title}, Created At: {job.created_at}")

import sys
import os
# from app import create_app, db
# Add the backend directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


app=create_app()
db.session.commit()

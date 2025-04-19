from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # Hashed password

    # def set_password(self, password):
    #     self.password = generate_password_hash(password)

    # def check_password(self, password):
    #     return check_password_hash(self.password, password)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(255), nullable=False, default='unknown')
    url = db.Column(db.String(512), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "location": self.location,
        }
    

# Utility functions to hash and verify password
def hash_password(password):
    return generate_password_hash(password)

def verify_password(password, hashed_password):
    return check_password_hash(hashed_password, password)


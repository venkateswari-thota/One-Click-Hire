from flask import Flask, request, jsonify
from flask_cors import CORS
from model import get_model_response
import re

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from React frontend

@app.route('/')
def home():
    return "Flask backend is running!"  

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    user_query = data.get("query", "").strip()

    # Get response from the model
    model_response = get_model_response(user_query)
    
    return jsonify({"response": model_response})  

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001, debug=True)

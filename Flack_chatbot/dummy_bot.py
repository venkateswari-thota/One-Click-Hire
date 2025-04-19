import re
import requests

# Replace with your actual Groq API key
GROQ_API_KEY = "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"

# Groq API setup
API_URL = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json",
}

# Predefined responses
responses = {
    r".(how\s+are\s+you).":"I am AgriBot. Here to assist you with agricultural solutions!",
    r".(who\s+are\s+you).":"I am AgriBot, created to serve farmers with solutions in agriculture.",
    r".(who\s+made\s+you).":"I am a creation of the Agro Team: T. Venkateswari, S. Lahari, and SK. Asiya Tabasum.",
    r"^(who\s+are\s+you|could\s+you\s+tell\s+me\s+who\s+are\s+you|what\s+is\s+your\s+name)\??$":
        "I am AgriBot, a chatbot developed by the Agro Team, students from IIIT-Nuzvid (Rajiv Gandhi University of Knowledge Technologies, Nuzvid).",
    r"^(how\s+are\s+you)\??$":
        "I am just a chatbot, but I'm here to help farmers with agricultural queries! How can I assist you today?",
    r"^(who\s+made\s+you|who\s+created\s+you)\??$":
        "I was made by the Agro Team: T. Venkateswari, S. Lahari, and SK. Asiya Tabasum, CSE students at IIIT-Nuzvid, Engineering 3rd year.",
    r"^(how\s+did\s+you\s+make\s+this|how\s+did\s+you\s+build\s+this)\??$":
        "I was built using the Mixtral-8x7B-32768 model to provide agricultural predictions and recommendations.",
    r"^(what\s+is\s+mixtral-8x7b-32768|tell\s+me\s+about\s+mixtral-8x7b-32768)\??$":
        "Mixtral-8x7B-32768 is an advanced AI model that helps me process and respond to agricultural queries efficiently.",
    r"^(how\s+do\s+you\s+work|how\s+do\s+you\s+function)\??$": 
        "I work by processing your agricultural queries through the Mixtral-8x7B-32768 model and generating relevant responses.",
    r"^(got\s+it|do\s+you\s+understand)\??$": 
        "Yes, I understand! How can I help you further?",
    r"^(what\s+can\s+you\s+do|what\s+are\s+your\s+abilities)\??$":
        "I specialize in agricultural predictions, crop recommendations, fertilizer suggestions, price forecasting, and weather reports.",
    r"^(how\s+old\s+are\s+you|when\s+were\s+you\s+created)\??$":
        "I am a creation of the Agro Team and continuously improving to serve farmers better.",
    r"^(what\s+is\s+your\s+purpose|why\s+do\s+you\s+exist)\??$":
        "My purpose is to assist farmers by providing data-driven agricultural solutions.",
    r"^(can\s+you\s+learn|are\s+you\s+learning)\??$":
        "Yes, I improve over time by learning from agricultural trends and queries.",
    r"^(do\s+you\s+have\s+feelings|are\s+you\s+alive)\??$":
        "No, I am an AI model and don't have feelings, but I can help farmers with their queries.",
    r"^(thank\s+you|thanks)\??$": 
        "You're welcome! I'm happy to assist with agricultural needs. Feel free to ask anything!",
    r"^(goodbye|bye|see\s+you)\??$": 
        "Goodbye! Have a great day! Keep farming smartly with AgriBot!",
    r"^(what\s+is\s+your\s+creator\s+name|who\s+is\s+your\s+maker)\??$":
        "My creators are T. Venkateswari, S. Lahari, and SK. Asiya Tabasum, students of CSE, E3 at IIIT-Nuzvid.",
    r"^(can\s+you\s+tell\s+me\s+the\s+implementation\s+details\s+of\s+yours\??)$":
        "I am powered by the Mixtral-8x7B-32768 model, developed to assist with agricultural solutions.",
    r"^(where\s+are\s+you)\??$":
        "I am running on the Agro Team's local system."
}


# Function to get response from Groq API (Mixtral-8x7B)
def get_ai_response(user_query):
    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": "You are an AI assistant specialized in agriculture, providing insights for farmers."},
            {"role": "user", "content": user_query},
        ],
        "temperature": 0.7,
    }

    response = requests.post(API_URL, json=payload, headers=HEADERS)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"

# Chat loop
print("\n🟢 AgriBot is active! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ").strip().lower()

    if user_input == "exit":
        print("🔴 AgriBot: Goodbye! Keep farming smart! 👋")
        break

    # Check predefined responses
    matched_response = None
    for pattern, response in responses.items():
        if re.match(pattern, user_input):
            matched_response = response
            break

    # If found in predefined responses, use that, else query Mixtral
    if matched_response:
        print(f"🤖 AgriBot: {matched_response}")
    else:
        print("🤖 AgriBot (AI):", get_ai_response(user_input))

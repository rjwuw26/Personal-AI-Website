"""
app.py
Author: Ryan Wilkerson
Version: 10/3/2025
Description: Main application file for the backend service.
"""

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_model import PersonalAI

# CORS allows frontend requests from different origins
app = Flask(__name__)
CORS(app)

# Initialize the AI model and personal context for inference
ai_model = PersonalAI()

@app.route('/ask', methods=['POST'])
def ask_ai():
    """
    Handles POST requests to the /ask endpoint.

    - Expects a JSON payload with a 'question' field.
    - Passes the question to the AI model for processing.
    - Returns the AI's response in JSON format.
    """
    data = request.json
    question = data.get('question', '')
    if not question:
        return jsonify({"error": "No question provided"}), 400
    
    try:
        response = ai_model.answer_question(question)
    except Exception as e:
        print(f"[ERROR] {e}")
        return jsonify({"error": "AI failed to generate a response"}), 500
    return jsonify({"answer": response})

# Launches Flash app on specified port
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
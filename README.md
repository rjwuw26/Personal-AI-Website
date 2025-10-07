Author: Ryan Wilkerson

Version: 1.0.0

Built with Llama 3.2-3B Instruct

This project uses **Meta Llama 3.2**, a large language model released by Meta under the **Llama 3.2 Community License Agreement**.  
Llama 3.2 is licensed under the [Llama 3.2 Community License](https://www.llama.com/llama3_2/license)  
**Copyright © Meta Platforms, Inc. All Rights Reserved.**

Use of Llama 3.2 and its outputs is subject to Meta’s [Acceptable Use Policy](https://www.llama.com/llama3_2/use-policy).

Desc: A full-stack personal website with a built in AI assistant designed to answer questions about
Ryan Wilkerson. The system uses a Flask backend integrated with a local LLaMA 3.2-3B-Instruct model from Hugging Face,
with embeddings powered by SentenceTransformers and vector search via FAISS.
The frontend provides an interactive chat that lets users naturally learn more about Ryan through AI-generated responses.

---

Project Plan - This is the plan I developed and followed throughout the course of this project.

Stage 1: Backend AI Development Prototype

Goal: Establish a functional AI logic module that operates independently.  
Status: Done  
Outcome: A working AI module capable of generating responses.

Tasks:
- Created the `PersonalAI` class in `ai_model.py`
- Implemented the `get_response()` method
- Tested locally using a `while True` loop


Stage 2: Flask Backend Skeleton

Goal: Set up a server to connect the frontend interface with the AI.  
Status: Done  
Outcome: The AI can now be queried via HTTP requests, enabling smooth frontend integration.

Tasks:
- Created `app.py` using Flask
- Imported and instantiated the `PersonalAI` class
- Defined an API route (`/ask`) to handle POST requests
- Returned structured JSON responses from the AI
- Tested endpoints using Postman and an early frontend prototype


Stage 3: Local Frontend Prototype

**Goal:** Build a functional website interface for interacting with the AI.  
**Status:** Done  
**Outcome:** Users can input questions and receive AI responses directly through the website.

Tasks:
- Designed basic HTML sections (About, Projects, Skills, Contact, AI Q&A)
- Added an input box and submission button for user queries
- Implemented a JavaScript `fetch()` call to the `/ask` endpoint
- Displayed AI responses dynamically on the webpage


Stage 4: AI Upgrade / Real Model Integration

Goal: Replace the prototype AI with a real pretrained model and personal context.  
Status: Done  
Outcome: The AI provides contextual and intelligent responses based on integrated personal data.

Tasks:
- Selected `Llama 3.2 3B Instruct` as the foundation model
- Integrated personal context (resume, project summaries, etc.)
- Replaced the placeholder logic in `get_response()` with real inference
- Conducted local accuracy and performance testing


Stage 5: Frontend Polishing and Styling

Goal: Refine the website design for a professional and responsive appearance.  
Status: Done  
Outcome: A portfolio-ready website featuring integrated AI capabilities.

Tasks:
- Applied modern CSS styling for visual consistency
- Ensured full responsiveness for both desktop and mobile devices
- Added optional visual enhancements such as animations and chat-like AI responses

---

Running the Project - Below are two viable options for running this project locally

Option One: 

Demo Mode - This mode lets anyone instantly try the website without needing a Hugging Face account or heavy model files.

1. Download the files from GitHub and extract anywhere on your computer. Open 'backend' folder in VS Code, terminal, or any workspace.

2. (Optionl) Create a virtual environment:

     `python -m venv venv`

   To activate:

     Windows: `venv\Scripts\activate`
     Linux: `source venv/bin/activate`

3. Install dependencies - Inside the "backend" folder, run:

     `pip install -r requirements.txt`

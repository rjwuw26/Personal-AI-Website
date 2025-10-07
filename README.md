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

3. Install dependencies - Ensure you have Python 3.10+ installed, inside the "backend" folder, run:

     `pip install -r requirements.txt`

4. Ensure ai_model.py is in Demo Mode - to run the code in demo mode, simply uncomment the answer_question() method with the "Demo" label and comment out the other method below it with the "full version" label.

5. Run the backend server - Start the Flask app by running:

     `python app.py`

   You should see output like:

   ` * Running on all addresses (0.0.0.0)`
   ` * Running on http://127.0.0.1:5000`
   ` * Running on http://192.168.1.20:5000`

6. Next, start the frontend by navigating to "aboutme.html". Right click anywhere in the file and click "Open with Live Server" (you can also do this by right clicking the file name in the file explorer in VS Code).

   This will open your browser to:

     `http://127.0.0.1:5500/frontend/aboutme.html`

7. You can now freely navigate the application's pages as well as interact with the AI to get quick and simple responses for quick viewing.

8. (Optional) To directly interact with the AI in the console, run:

     `python ai_model.py`


Option Two:

Full Version - By default, the project is already in Full Version. Make no changes to the code in `ai_model.py`.

**Important Note:** This option requires a Hugging Face account and explicit access to the LLaMA 3.2 3B Instruct model. Without this, the code will not be able to load the model.

1. Download the files from GitHub and extract anywhere on your computer. Open 'backend' folder in VS Code, terminal, or any workspace.

2. (Optionl) Create a virtual environment:

     `python -m venv venv`

   To activate:

     Windows: `venv\Scripts\activate`
     Linux: `source venv/bin/activate`

3. Install dependencies - Ensure you have Python 3.10+ installed, inside the "backend" folder, run:

     `pip install -r requirements.txt`

4. Acquire permission from Hugging Face:

   - Navigate to https://huggingface.co/
   - Create a free account if you don't already have one
   - Navigate to the LLaMA 3.2 3B Instruct model page: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct
   - Click "Access Repository" (or similar) and follow instructions
   - Accept the LLaMA 3.2 Community License to gain permission to use the model

   (Note: permission will take time, between an 1 to 24 hours after submission)

5. Generate Personal Access Token

   - Go to your Hugging Face Settings and find Access Tokens
   - Click "New Token", give it a name and select `read` permissions.
   - Copy the generated token - you'll need it in the next step.

6. Configure Project

   - Inside the backend folder of the project, create a .env file.
   - Add your Hugging Face token like this:

          `HF_TOKEN=hf_your_personal_token_here`

7. Run the Frontend - In the "frontend" folder, open any HTML file (e.g., aboutme.html) in your browser, or use Live Server in VS Code for dynamic updates and navigate the application or ask questions to the AI.


Figure 1: Home page (aboutme.html)

<img width="1500" height="800" alt="image" src="https://github.com/user-attachments/assets/689fb30e-a2e7-4d0c-a700-65e3c976e7af" />

Figure 2: Contact page (contact.html)

<img width="1500" height="800" alt="image" src="https://github.com/user-attachments/assets/75ff5642-3a94-4ce6-93f9-46d6b9dd0ba0" />



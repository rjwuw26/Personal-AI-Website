"""
ai_model.py
Author: Ryan Wilkerson
Version: 10/3/2025
Description: AI model handling and inference logic for personal website.
"""

import os
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from config import MODEL_NAME, TOP_K, MAX_NEW_TOKENS, PERSONAL_DATA_FOLDER, HF_TOKEN, DEVICE

class PersonalAI:
    """
    Uses FAISS for semantic search over personal data and LLaMA for natural language generation.
    """

    def __init__(self, model_name = MODEL_NAME, device = DEVICE):
        """
        Initialize the AI model, load personal data, and create FAISS index.

        - Loads personal data from text files from specified folder.
        - Encodes text chunks using SentenceTransformer to create embeddings.
        - Builds a FAISS index for efficient similarity search.
        - Loads LLaMA model and tokenizer from Hugging Face.
        """
        # Load personal data
        self.texts = self.load_personal_data(PERSONAL_DATA_FOLDER)
        if not self.texts:
            raise RuntimeError(f"No personal data loaded. Check folder: {PERSONAL_DATA_FOLDER}")

        # Build FAISS index
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.embeddings = self.embedding_model.encode(self.texts, convert_to_numpy=True)
        dimension = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(self.embeddings)
        print(f"[INFO] Loaded {len(self.texts)} text chunks and created FAISS index (dim={dimension}).")

        # Load LLaMA model and tokenizer
        self.device = device
        self.tokenizer, self.model = self.load_llama_model(model_name)

    def load_llama_model(self, model_name):
        """
        Loads LLaMA model and tokenizer from Hugging Face.

        - Uses provided model name and authentication token.
        - Automatically maps model to available device (GPU/CPU).
        - Ensures tokenizer has a padding token.
        - Returs tokenizer and model.
        """
        print(f"[INFO] Loading {model_name} on {self.device} ...")
        tokenizer = AutoTokenizer.from_pretrained(model_name, token=HF_TOKEN)
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map="auto",
            torch_dtype=torch.float16,
            token=HF_TOKEN
        )

        print("LLaMA model loaded successfully.")
        return tokenizer, model

    def load_personal_data(self, folder):
        """
        Load and splits personal text data from .txt files in the specified folder.

        - Each file is split into chunks based on double newlines.
        - Stripes leading/trailing whitespace from each chunk.
        - Returns a list of text chunks.
        """
        if not os.path.exists(folder):
            raise FileNotFoundError(f"{folder} does not exist. Place your text files there.")

        texts = []
        for filename in os.listdir(folder):
            if filename.endswith(".txt"):
                with open(os.path.join(folder, filename), "r", encoding="utf-8") as f:
                    chunks = f.read().split("\n\n")
                    texts.extend([chunk.strip() for chunk in chunks if chunk.strip()])
        return texts

    # DEMO: Version of answer_question() without LLaMA generation for quick view and demo. Uncomment this version to use and comment out the other.
    """
    def answer_question(self, question: str) -> str:
        # Hardcoded list of projects (only used for list-style questions)
        project_list = [
            "• Personal Website with LLM Integration",
            "• MultiView Synchro (HCI Class Project)",
            "• Privacy and Security of Drones (Ethics Paper)",
            "• Recipe Book Web App"
        ]
        qlow = question.lower()
        if any(k in qlow for k in ["list", "projects", "portfolio", "what projects", "name projects"]):
            return "\n".join(project_list)

        # Embed the question and do FAISS search
        q_emb = self.embedding_model.encode([question], convert_to_numpy=True)
        # use TOP_K from config or hardcode small k
        distances, indices = self.index.search(q_emb, min(5, len(self.texts)))
        context_chunks = [self.texts[int(i)] for i in indices[0] if int(i) < len(self.texts)]
        # Join the top chunks and return a trimmed response
        context_text = "\n\n".join(context_chunks).strip()
        if not context_text:
            return "I don't know."
        # Short summary fallback: return top chunk or the first ~400 chars
        top = context_chunks[0].strip()
        return top if len(top) < 500 else top[:500].rsplit(" ", 1)[0] + "..."
    """
    
    # Note: This is the full version of answer_question() with LLaMA generation. Comment out this version to use the simpler one above.
    def answer_question(self, question: str) -> str:
        """
        Answers a question using the personal data and LLaMA model generation.

        - Checks for project-related keywords to return a hardcoded list of projects.
        - Embeds the question and retrieves top relevant text chunks from FAISS.
        - Constructs a prompt with context and question for the LLaMA model.
        - Tokenizes the prompt and generates a response.
        - Extracts and returns the most relevant sentence from the response.

        Returns: A string answer to the question.
        """
        # Hardcoded fallback list of projects
        project_list = [
            "• Personal Website with LLM Integration",
            "• MultiView Synchro (HCI Class Project)",
            "• Privacy and Security of Drones (Ethics Paper)",
            "• Recipe Book Web App"
        ]

        # Check for project-related keywords
        if any(keyword in question.lower() for keyword in ["list", "name", "projects", "portfolio", "examples"]):
            return "\n".join(project_list)

        # Embed the question
        question_embedding = self.embedding_model.encode([question], convert_to_numpy=True)

        # Search FAISS for top 3 relevant chunks
        distances, indices = self.index.search(question_embedding, 10)
        context_chunks = [self.texts[int(i)] for i in indices[0].tolist()]        
        context_text = "\n".join(context_chunks)

        # Build prompt with clear context instructions
        messages = [
            {"role": "system", "content": "You are a friendly and knowledgeable assistant answering questions about Ryan Wilkerson. Answer naturally with personality, without mentioning the context or how you found the answer. If you don't know the answer, just say 'I don't know.'"},
            {"role": "user", "content": f"Context:\n{context_text}\n\nQuestion: {question}"}
        ]

        # Apply chat template
        prompt_text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        # Tokenize with chat template
        inputs = self.tokenizer(
            prompt_text,
            return_tensors="pt",
            truncation=True,
            max_length=1024,
            padding=True
        ).to(self.device)

        # Generate response
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=MAX_NEW_TOKENS,
            do_sample=False,
            pad_token_id=self.tokenizer.eos_token_id
        )

        # Decode and extract first sentence
        raw_output = self.tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

        # Extract the most relevant line from the output
        lines = raw_output.split("\n")
        for line in reversed(lines):
            if line.strip() and not line.strip().startswith("<") and "answer" not in line.lower():
                return line.strip()
        return "I'm not sure about that. Could you ask in a different way?"


if __name__ == "__main__":
    """
    Launches the interactive console for testing the PersonalAI class.
    - Initializes the PersonalAI instance.
    - Continuously prompts the user for questions until 'quit' or 'exit' is entered.
    - Exits when the user types 'quit' or 'exit'.
    """
    ai = PersonalAI()
    print("Personal AI is ready! Type 'quit' or 'exit' to stop.\n")
    while True:
        q = input("Ask something: ").strip()
        if q.lower() in ["quit", "exit"]:
            break
        print("\nAI:", ai.answer_question(q), "\n")



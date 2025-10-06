"""
config.py
Author: Ryan Wilkerson
Version: 10/3/2025
Description: Configuration settings for personal website backend AI.
"""

import os
import torch
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
HF_TOKEN = os.getenv("HF_TOKEN")
"""
# MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf" # Original LLaMA 2-7B Chat
# MODEL_NAME = "meta-llama/Llama-3.2-3B" # swap to 3B or 7B easily
"""
MODEL_NAME = "meta-llama/Llama-3.2-3B-Instruct" # Current working model for personal website
TOP_K = 5
MAX_NEW_TOKENS = 300
PERSONAL_DATA_FOLDER = "personal_data"  # Folder containing personal .txt files
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
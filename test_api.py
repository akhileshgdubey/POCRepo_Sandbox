import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("API key not found! Check your .env file.")
else:
    print("API Key loaded successfully!")
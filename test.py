import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Test to see if the API key is loaded correctly
api_key = os.getenv("ELEVENLABS_API_KEY")
if api_key:
    print("API Key loaded successfully!")
else:
    print("Failed to load API Key.")

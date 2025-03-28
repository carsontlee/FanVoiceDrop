import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Retrieve your API key from the environment variables
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Check if the API key is loaded correctly
if ELEVENLABS_API_KEY is None:
    print("Error: ELEVENLABS_API_KEY is not set. Check your .env file.")
else:
    print(f"Your API Key: {ELEVENLABS_API_KEY}")

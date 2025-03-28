import os
from dotenv import load_dotenv
import requests


# Load environment variables from .env file
load_dotenv()

# Retrieve the variables
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")

# Debug: Print to confirm they're being read properly
print(f"API Key: {ELEVENLABS_API_KEY}")
print(f"Voice ID: {ELEVENLABS_VOICE_ID}")

# Get your ElevenLabs API key from the .env file
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
if not ELEVENLABS_API_KEY:
    raise ValueError("API key not found. Please add your ELEVENLABS_API_KEY to your .env file.")

# Set the API endpoint URL for ElevenLabs
ELEVENLABS_URL = "https://api.elevenlabs.io/v1/text-to-speech/THrrYJ44O9C483TCaDKL"

# User Input
user_prompt = input("Enter a creative phrase you want to hear generated (e.g., 'Welcome to the show!'): ")

# API Request to ElevenLabs
headers = {
    "Content-Type": "application/json",
    "xi-api-key": ELEVENLABS_API_KEY
}

data = {
    "text": user_prompt,
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
    }
}

response = requests.post(ELEVENLABS_URL, headers=headers, json=data)

# Check if the request was successful
if response.status_code == 200:
    # Save the audio file to the local folder
    with open("generated_audio.mp3", "wb") as audio_file:
        audio_file.write(response.content)
    print("✅ Audio generated and saved as 'generated_audio.mp3'.")
else:
    print(f"❌ Error {response.status_code}: {response.json()}")

# FanVoice Drop Tool
### A Proof-of-Concept Tool to Transform Fan Recordings into Live Show Audio Clips using ElevenLabs API

## Overview
The **FanVoice Drop Tool** is a conceptual project aimed at enhancing fan engagement before and during live shows. Using ElevenLabs’ Voice AI technology, this tool allows artists and DJs to:

1. Collect voice recordings from fans before a show.
2. Use ElevenLabs’ API to generate custom phrases spoken in the fan’s voice.
3. Play these clips during live performances to create unforgettable moments for fans, while giving artists a fun, creative way to customize each show to their audience.

## Use Case
Imagine a DJ like Dom Dolla playing his song "San Francisco" at a show. In the original recording of the song, there is a voice that says "San Francisco, where's your disco" right before the beat drops. 

Instead, imagine a lucky fan's voice saying that same line, but "San Francisco" is swapped with the city the show is at.

Take it a step further - the fan's voice could say any custom hype phrase that the artist wants, inserted at any point in any song during the show. 

## Why This Matters
This proof-of-concept tool showcases the potential of utilizing voice AI to transform fan experiences and deepen the connection between artists and their audience. It highlights an innovative approach to fan engagement by making each performance interactive, unique, and unforgettable. 

The music industry is increasingly building products and experiences to serve the "superfan". What are superfans' wildest wishes that artists can make come true? One category of fan wishes is to be able to co-create with their favorite artists. Imagine hearing your voice layered creatively into your favorite artist's live set!

From the artist perspective, this tool opens up new possibilities for marketing and fan engagement. For example, artists can invite fans to submit voice recordings, with the chance to be featured as the lucky voice played during a show. Artists can also crowdsource creative text prompts from fans, further elevating this unique collaboration between the artist and fan. During a performance, voice AI unlocks unprecedented levels of recorded voice customization, creating moments of surprise and delight that fans crave.

Ultimately, voice AI empowers us to explore the limitless magic of music and create unforgettable memories together.

## Tools & Technologies
- Programming Language: Python (Simple script provided)
- APIs Used: [ElevenLabs VoiceLab API](https://elevenlabs.io/docs/overview)

## Repository Contents
- fanvoice_tool.py - Python script to interact with the ElevenLabs API and generate fan voice clips.
- sample_audio_files - Folder containing generated audio clips created by the tool for demonstration purposes.
- requirements.txt - File listing the necessary packages to run the script (requests and python-dotenv).
- .gitignore - File to exclude sensitive files (e.g., .env and venv/) from being uploaded to your GitHub repository.
- .env - File containing your ElevenLabs API key and VOICE_ID (not included in the repo for security reasons).

## **How To Use**
1. **Set Up Your ElevenLabs API Key & Voice ID**  
   - Create an `.env` file in the root of the project directory (same level as `fanvoice_tool.py`).
   - Add the following lines to your `.env` file:
     ```bash
     ELEVENLABS_API_KEY=your_api_key_here
     ELEVENLABS_VOICE_ID=your_voice_id_here
     ```
   - Replace `your_api_key_here` with your actual ElevenLabs API key.
   - Replace `your_voice_id_here` with the Voice ID from ElevenLabs' VoiceLab (from your uploaded fan voice sample).

2. **Install Dependencies**  
   - Install the necessary packages by running:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Script**  
   - Make sure your virtual environment is activated:
     ```bash
     source venv/bin/activate  # For MacOS/Linux
     .\venv\Scripts\activate    # For Windows
     ```
   - Run the script with:
     ```bash
     python3 fanvoice_tool.py
     ```

4. **Generate Audio Clips**  
   - Enter the creative phrase you want the fan’s voice to say (e.g., **"San Francisco, Where's Your Disco"**).
   - The generated audio clip will be saved automatically in the root of the project directory as an `.mp3` file.

## Future Vision
This project is a work-in-progress, with several exciting potential improvements to explore:

- Integrating Google’s TextFX API to generate creative text prompts
- Building a simple web application where fans submit recordings directly.
- Developing a broader fan engagement platform where artists crowdsource text prompts from fans and remix them with ElevenLabs' audio technology.

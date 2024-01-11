# Author: nn-n
# Date: January 2024
# Version: 3.5

import speech_recognition as sr
from googlesearch import search

# Initialize the speech recognizer
recognizer = sr.Recognizer()

def get_audio_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand. Please try again.")
        return ""

    except sr.RequestError:
        print("Error: Speech recognition service is unavailable. Try checking your internet connection!(｡•́︿•̀｡)")
        return ""

def search_google(query):
    try:
        print(f"Searching Google for: {query}")
        for j in search(query, num_results=5, lang="en"):
            print(j)

    except Exception as e:
        print(f"Error: {e}")

# Get user command using speech recognition
user_command = get_audio_input()
print(f"Received command: {user_command}")

if "search Google for" in user_command:
    query = user_command.replace("search Google for", "").strip()
    search_google(query)
else:
    print("No search command detected.")

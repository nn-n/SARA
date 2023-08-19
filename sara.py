import datetime
import speech_recognition as sr

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
        print("Sorry, I couldn't understand.")
        return ""

    except sr.RequestError:
        print("Sorry, my speech recognition service is unavailable.")
        return ""

# Continuous interaction loop
while True:
    # Get user command using speech recognition
    user_command = get_audio_input()

    # Check if the user wants to exit
    if user_command.lower() == "exit":
        break

    # Check if the user wants to know the time
    if "what time is it" in user_command.lower():
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Current time is:", current_time)

"""User

import requests
import openai
import speech_recognition as sr

# Set your OpenAI API key
openai.api_key = "enter-your-own-key"

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
        print("Sorry, I couldn't understand.")
        return ""

    except sr.RequestError:
        print("Sorry, my speech recognition service is unavailable.")
        return ""

def get_chatgpt_response(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    payload = {
        "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}],
        "max_tokens": 50  # Adjust the desired response length
    }

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=payload["messages"],
            max_tokens=payload["max_tokens"]
        )
        chatgpt_response = response.choices[0].message.content.strip()
        return chatgpt_response

    except requests.RequestException as e:
        print("Error:", e)
        return "Sorry, I'm having trouble generating a response."

# Continuous interaction loop
while True:
    # Get user prompt using speech recognition
    user_prompt = get_audio_input()

    # Check if the user wants to exit
    if user_prompt.lower() == "exit":
        break

    # Generate ChatGPT response
    chatgpt_response = get_chatgpt_response(user_prompt)
    print("AI:", chatgpt_response)

"""
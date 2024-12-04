# Author: nn-n
# Date: December 2024
# Version: 4.1

import random
import speech_recognition as sr
from googlesearch import search
from bs4 import BeautifulSoup
import requests

# Initialize the speech recognizer
recognizer = sr.Recognizer()

QUESTION_WORDS = ["what", "who", "where", "when", "why", "how", "search", "display"]
THANK_YOU_RESPONSES = ["No problem!", "You're welcome!", "Glad to help!", "Anytime!", "Happy to assist!"]

def get_audio_input():
    """
    Captures audio input from the user and converts it to text using Google Speech Recognition.
    """
    with sr.Microphone() as source:
        print("\nListening for a command...")
        audio = recognizer.listen(source)  # No timeout parameter

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand. Please try again.")
        return ""

    except sr.RequestError:
        print("Error: Speech recognition service is unavailable. Check your internet connection.")
        return ""


import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup

def get_full_article(url):
    """
    Extracts the full article from the webpage at the provided URL.
    """
    try:
        # Send an HTTP request to the URL
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Try to extract the main content area by looking for typical article tags
        # Adjust these selectors depending on the website you're working with
        article_content = soup.find(['article', 'div', 'main'], class_=['article', 'content', 'post-body', 'entry-content', 'article-body'])

        # If no article content found, fall back to extracting text from all <p> tags
        if article_content:
            paragraphs = article_content.find_all('p')
            full_article = "\n".join([p.get_text() for p in paragraphs])
            return full_article.strip()

        # Fallback: If no content found, extract text from all <p> tags on the page
        paragraphs = soup.find_all('p')
        if paragraphs:
            full_article = "\n".join([p.get_text() for p in paragraphs])
            return full_article.strip()

        return "Full article not available for this page."

    except Exception as e:
        return f"Error fetching article: {e}"






import time

def search_google(query):
    """
    Searches Google for the provided query and displays the full article of the first result.
    """
    try:
        print(f"\nSearching for: {query}\n")
        results = [result for result in search(query, num_results=1, lang="en")]
        if results:
            first_result = results[0]
            print(f"Top result: {first_result}")

            full_article = get_full_article(first_result)
            print(f"\nFull Article:\n{full_article}")

        else:
            print("No results found.")
    except Exception as e:
        print(f"Error during Google search: {e}")



def main():
    print("Hello! How can I help? \n")
    print("You can say commands like 'search Google for ...' or ask questions starting with 'what', 'who', etc. \n")
    print("Say 'quit' to exit.\n")

    while True:
        # Get user command
        user_command = get_audio_input().lower()

        # Check for exit command
        if "quit" in user_command or "exit" in user_command:
            print("Exiting SARA. Goodbye!")
            break

        # Check for "Thank You, SARA" (or similar)
        if "thank you sara" in user_command or "thank you, sara" in user_command or "thank you sarah" in user_command:
            response = random.choice(THANK_YOU_RESPONSES)
            print(response)
            continue

        # Check if the command starts with a question word
        for word in QUESTION_WORDS:
            if user_command.startswith(word):
                query = user_command  # Use the entire input as the query
                search_google(query)
                break
        else:
            # Handle 'search Google for'
            if "search Google for" in user_command:
                query = user_command.replace("search Google for", "").strip()
                if query:
                    search_google(query)
                else:
                    print("No query provided. Please try again.")
            else:
                # Unrecognized command
                print("I didn't catch that. You can try asking a question or saying 'search Google for ...'.\n")

if __name__ == "__main__":
    main()

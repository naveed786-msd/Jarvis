import requests
import pyttsx3
import speech_recognition as sr
from datetime import datetime
from random import choice
from pprint import pprint

# Importing from other files
from functions.online_ops import (
    find_my_ip, get_latest_news, get_random_advice,
    get_random_joke, get_trending_movies, get_weather_report,
    play_on_youtube, search_on_google, search_on_wikipedia,
    send_email, send_whatsapp_message
)
from functions.os_ops import (
    open_calculator, open_camera, open_cmd,
    open_notepad, open_discord
)
from utils import opening_text

# ----------------- Settings -----------------
USERNAME = "Naveed"
BOTNAME = "Jarvis"

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 190)   # Rate
engine.setProperty('volume', 1.0) # Volume
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

# ----------------- Functions -----------------
def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def greet_user():
    """Greets the user according to the time."""
    hour = datetime.now().hour
    if 6 <= hour < 12:
        speak(f"Good Morning {USERNAME}")
    elif 12 <= hour < 16:
        speak(f"Good afternoon {USERNAME}")
    elif 16 <= hour < 19:
        speak(f"Good Evening {USERNAME}")
    else:
        speak(f"Hello {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")

def take_user_input():
    """Takes voice input and converts it to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        if "exit" in query or "stop" in query:
            hour = datetime.now().hour
            if 21 <= hour or hour < 6:
                speak("Good night sir, take care!")
            else:
                speak("Have a good day sir!")
            exit()
        else:
            speak(choice(opening_text))
            return query.lower()
    except Exception:
        speak("Sorry, I could not understand. Could you please say that again?")
        return "None"

# ----------------- Main Program -----------------
if __name__ == "__main__":
    greet_user()
    while True:
        query = take_user_input()

        if "open notepad" in query:
            open_notepad()

        elif "open discord" in query:
            open_discord()

        elif "open command prompt" in query or "open cmd" in query:
            open_cmd()

        elif "open camera" in query:
            open_camera()

        elif "open calculator" in query:
            open_calculator()

        elif "ip address" in query:
            ip_address = find_my_ip()
            speak(f"Your IP Address is {ip_address}. For your convenience, I am printing it on the screen sir.")
            print(f"Your IP Address is {ip_address}")

        elif "wikipedia" in query:
            speak("What do you want to search on Wikipedia, sir?")
            search_query = take_user_input()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            print(results)

        elif "youtube" in query:
            speak("What do you want to play on Youtube, sir?")
            video = take_user_input()
            play_on_youtube(video)

        elif "search on google" in query:
            speak("What do you want to search on Google, sir?")
            search_query = take_user_input()
            search_on_google(search_query)

        elif "send whatsapp message" in query:
            speak("On what number should I send the message sir? Please enter in the console:")
            number = input("Enter number: ")
            speak("What is the message sir?")
            message = take_user_input()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        elif "send an email" in query:
            speak("On what email address do I send sir? Please enter in the console:")
            receiver = input("Enter email: ")
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            speak("What is the message sir?")
            message = take_user_input().capitalize()
            if send_email(receiver, subject, message):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail.")

        elif "joke" in query:
            joke = get_random_joke()
            speak(joke)
            pprint(joke)

        elif "advice" in query:
            advice = get_random_advice()
            speak(advice)
            pprint(advice)

        elif "trending movies" in query:
            movies = get_trending_movies()
            speak(f"Some of the trending movies are {movies}")
            print(*movies, sep="\n")

        elif "news" in query:
            news = get_latest_news()
            speak("Here are the latest headlines.")
            print(*news, sep="\n")

        elif "weather" in query:
            ip = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip}/city/").text
            speak(f"Getting weather report for {city}")
            weather, temp, feels_like = get_weather_report(city)
            speak(f"The temperature is {temp}, feels like {feels_like}. Weather is {weather}")
            print(f"Description: {weather}\nTemperature: {temp}\nFeels like: {feels_like}")

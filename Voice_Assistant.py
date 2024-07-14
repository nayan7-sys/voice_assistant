import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice', voices[1].id) 


def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return None

def respond_to_greeting():
    speak("Hello Sir! I am your voice assistant. How can I help you?")

def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    speak(f"The current time is {current_time}")

def tell_date():
    now = datetime.datetime.now()
    current_date = now.strftime("%B %d, %Y")
    speak(f"Today's date is {current_date}")

def search_web(query):
    speak(f"Searching the web for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def play_on_youtube(query):
    speak(f"Playing {query} on YouTube")
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

def main():
    speak("Voice assistant activated.")
    while True:
        command = listen()
        if command:
            if "hello" in command:
                respond_to_greeting()
            elif "time" in command:
                tell_time()
            elif "date" in command:
                tell_date()
            elif "search" in command:
                search_query = command.split("search")[1].strip()
                search_web(search_query)
            elif "play" in command:
                play_query = command.split("play")[1].strip()
                play_on_youtube(play_query)
            elif "exit" in command or "quit" in command:
                speak("Goodbye!")
                break

if __name__ == "__main__":
    main()


import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes


# Text to Speech
def speechx(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 160)

    engine.say(text)
    engine.runAndWait()


# Speech to Text
def sptext():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

            print("Recognizing...")

            data = recognizer.recognize_google(audio)
            print("You said:", data)

            return data.lower()

    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        return ""

    except sr.RequestError:
        print("Internet connection or speech service error.")
        return ""

    except sr.WaitTimeoutError:
        print("Listening timed out.")
        return ""

    except OSError:
        print("Microphone not found.")
        return ""


# Main Program
if __name__ == '__main__':

    speechx("Hello, I am AJ. How can I help you?")

    while True:

        data1 = sptext()

        if not data1:
            continue

        # Assistant Name
        if "your name" in data1:
            speechx("My name is AJ.")

        # Assistant Age
        elif "old are you" in data1:
            speechx("I am just 22 years old.")

        # Current Time
        elif "time" in data1:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speechx("The current time is " + time)

        # Current Date
        elif "date" in data1:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speechx("Today's date is " + date)

        # Open YouTube
        elif "youtube" in data1:
            speechx("Opening YouTube.")
            webbrowser.open("https://www.youtube.com/")

        # Open WhatsApp
        elif "whatsapp" in data1:
            speechx("Opening WhatsApp.")
            webbrowser.open("https://web.whatsapp.com/")

        # Open ChatGPT
        elif "chatgpt" in data1:
            speechx("Opening ChatGPT.")
            webbrowser.open("https://chatgpt.com/")

        # Play Song
        elif "song" in data1 or "music" in data1:
            speechx("Playing your favourite song.")
            webbrowser.open(
                "https://www.youtube.com/watch?v=fFLWgtL9OAI"
            )

        # Tell a Joke
        elif "joke" in data1:
            joke = pyjokes.get_joke(
                language="en",
                category="neutral"
            )
            print("AJ:", joke)
            speechx(joke)

        # Open Google
        elif "google" in data1:
            speechx("Opening Google.")
            webbrowser.open("https://www.google.com/")

        # Open Instagram
        elif "instagram" in data1:
            speechx("Opening Instagram.")
            webbrowser.open("https://www.instagram.com/")

        # Exit Assistant
        elif "exit" in data1 or "stop" in data1 or "bye" in data1:
            speechx("Thank you. Have a good day. Bye bye!")
            break

        # Unknown Command
        else:
            print("Sorry, I don't understand that command.")
            speechx("Sorry, I don't understand that command.")

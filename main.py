import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio =recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data

        except sr.UnknownValueError:
            return ""
            print("Not Understanding ")

def speechx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rete =engine.getProperty('rate')
    engine.setProperty('rate',160)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':

  #if sptext().lower() == "hay aj ":
     while True:
        data1=sptext().lower()

        if "your name" in data1:
            name = "may name is aj"
            speechx(name)

        elif "old are you" in data1:
             age = "i am just 22 years old"
             speechx(age)
        elif 'time' in data1:
             time = datetime.datetime.now().strftime("%I%M%p")
             speechx(time)

        elif 'youtube' in data1:
             webbrowser.open("https://www.youtube.com/")
             
        elif 'whatsapp' in data1:
             webbrowser.open("https://web.whatsapp.com/")

        elif 'chatgpt' in data1:
             webbrowser.open("https://chatgpt.com/")
        
        elif 'song' in data1:
             webbrowser.open("https://www.youtube.com/watch?v=fFLWgtL9OAI&list=RDfFLWgtL9OAI&start_radio=1")
            
        elif 'joke' in data1:
             joke_1 = pyjokes.get_joke(language="en",category="neutral")
             print(joke_1)
             speechx(joke_1)

        elif "exit" in data1:
             speechx("thank you  have a good day, by love you.")
             break

        else:
          print("thank You have a good day, by love you. ")






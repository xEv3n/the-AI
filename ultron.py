from logging import exception
import datetime as dt

import wikipedia
import time
import pyttsx3
import speech_recognition as sr
import webbrowser
import os

    
def speak(prompt):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(prompt)
    engine.runAndWait()

def read():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)
    speak("what you want me to read")
    x = input("what you want me to read :")
    engine.say(x)
    engine.runAndWait()



time  = time.strftime("%H:%M:%S", time.localtime())
if time < str(12):
    speak("good morning")
elif time < str(12) and time > 16:
    speak("good afternoon")
elif time < str(16) and time > str(20):
    print('good evening')
else:
    speak("good night")

speak("how may I help you ")

date =  dt.datetime.now()
def say():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.energy_threshold = 500
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio,language = "en-IN")
        print(f"user said: {query}\n",sep=" ")




    except exception as e:
        print("please say that again ")
        

    return query


query = say().lower()

def calculator():
    speak("okay")

    speak("tell me your first number")

    print("tell me your first number :")
    a = say()
    a = int(a)


    speak("tell me your second number")
    b = say()
    b = int(b)

    speak("choose your operator among plus \n minus \n divide \n multiply")
    c = say()

    if "Plus" in c:
        print(f"your answer is {a+b}")
        speak(f"your answer is {a+b}")
        

    if "minus" in c :
        print(f"your answer is {a-b}")
        speak(f"your answer is {a-b}")
        

    if "divide" in c :
        print(f"your answer is {a/b}")
        speak(f"your answer is {a/b}")
        


    elif "multiply" in c :
        print(f"your answer is {a*b}")
        speak(f"your answer is {a*b}")
        

if "who are you" in query:
    speak("i am  ultron \n nice to meet you")

elif "hello" in query:
    speak("hello \n how are you")

elif "open youtube" in query:
    
    speak("opening youtube")
    webbrowser.open("https://www.youtube.com")

elif "date and time" in query:
    speak(f"current date and time is{date}")

elif "open google" in query:
    speak("opening google")
    webbrowser.open("www.google.com")

elif "wikipedia" in query:
    x = wikipedia.summary(query,sentences = 2)
    print(x)
    speak(f"according to wikipedia{x}")

elif "calculator" in query:
    calculator()

elif "stack overflow" in query:
    webbrowser.open("www.stackoverflow.com")



elif "brave"  in query:
    speak ("nahi chal raha bhaiee ")
    
elif "read" in query:
    read()     


































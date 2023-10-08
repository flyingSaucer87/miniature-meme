import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import pyaudio
import os


'''
Code by Vegeta2007k/Yogi
'''
# we create a variable 'listener' which will be our sr.Recognizer
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Defining a talk function
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Defining a take command function through which the AI will take commands
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...Created by @Yogi')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
        
    except:
        pass
    return command
# Defining the commands and their output
def run_jarvis():
    command = take_command()
    print("Recognizing...Created by @Yogi")
    print(command)
# A command to play music on YouTube
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

# A command to tell the time
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

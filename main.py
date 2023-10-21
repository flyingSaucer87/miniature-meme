import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import pyaudio
import os
import ctypes


'''
Code by Vegeta2007k/Yogi
'''
# we create a variable 'listener' which will be our sr.Recognizer
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newsURL = "https://news.google.com/search?q="

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

    except Exception:
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

# A command which will open youtube on google chrome
    elif 'youtube' in command:
        webbrowser.open("https://www.youtube.com/")
        talk("YouTube has been opened...")

# A command which uses the Wikipedia module to get information about people from wikipedia
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

# A command which will play...well..the best song (be surprised lol)
    elif 'best song' in command:
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        talk("There you go")

# A command to open reddit
    elif 'reddit' in command:
        webbrowser.open("https://www.reddit.com/")
        talk("Opening Reddit...")

# A command to lock windows or put it to sleep
    elif "windows" in command or "pc" in command or "computer" in command:
        if "lock" in command:  # lock windows
            talk("Locking windows in 5 seconds.")
            time.sleep(5)
            ctypes.windll.user32.LockWorkStation()  # call to lock windows

        elif "sleep" in command:  # sleep
            talk("Windows will go to sleep in 5 seconds.")
            time.sleep(5)
            # call to put windows to sleep
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

# A command to open news on a specific topic or just general news
    elif "news" in command or "headlines" in command:
        if "on" in command:  # check if news on specific topic
            command = command.split("on")[1]
            webbrowser.open_new_tab(newsURL + command)
            talk(f"Here are some headlines on {command}\n Happy Reading.")
        else:  # general news
            webbrowser.open_new_tab(newsURL)
            talk(
                'Here are some news headlines." \
                    "Happy reading'
            )

# A command to open spotify or search a song on spotify
    elif "spotify" in command or "search the song":
        if "spotify" in command:
            webbrowser.open_new_tab("https://open.spotify.com")
            talk("Opening Spotify...")
        else: #open spotify with a specific song
            songname = command.replace('search the song', '')
            webbrowser.open_new_tab("https://open.spotify.com/search/"+songname+"/tracks")
            talk("Searching the song on Spotify...")

'''
Like this, you can add up any command to open any website...
'''

while True:
    run_jarvis()
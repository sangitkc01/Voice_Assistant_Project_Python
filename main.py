import datetime

import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser as wb
import os
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except(Exception,):
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("Current time is " + time)
    elif 'date' in command:
        day = datetime.datetime.now().day
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year
        print(day, month, year)
        talk('the current date is ')
        talk(day)
        talk(month)
        talk(year)
    elif 'who the heck is' in command:
        person = command.replace("who the heck is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "open chrome" in command:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(chrome_path)
    # elif "search chrome on" in command:
    #     url = command.replace('search chrome on', '')
    #     chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    #     wb.get(chrome_path).open_new_tab(url+'.com')
    elif 'are you single' in command:
        talk('I am in relationship, you single boy.')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open google' in command:
        wb.open("google.com")
    else:
        talk('Please say the command again')

while True:
    run_alexa()

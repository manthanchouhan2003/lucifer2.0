import pyttsx3  # pip installpyttsx3 For Voice REcognization
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import subprocess
import json
import speech_recognition as sr
import wolframalpha
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture  import ecapture as ec
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')  # microsoft speaking module
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 200)


def speak(audio):
    print("     ")
    print(f"Lucifer :{audio}")
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good morning,sir")
    elif hour >= 12 and hour <= 18:
        speak("good afternoon,sir")
    else:
        speak("Good evvening,sir")
    speak("I am lucifer your personal assistent,sir,How may i help you.")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing....")
        quarry = r.recognize_google(audio, language='en-in')
        print(f"user said:{quarry}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return quarry


def sendEmail(to, subject, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('manthanchouhan2003@gmail.com', 'bftuehdswtwidvjg')
    server.sendmail('manthanchouhan2003@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        quarry = takeCommand().lower()

        if "wikipedia" in quarry:
            speak("I am searching it sir,")
            quarry = quarry.replace("wikipedia", "")
            results = wikipedia.summary(quarry, sentences=1)
            speak("Sir, according to wikipedia..")
            speak(results)
        elif "open youtube" in quarry:
            webbrowser.open("you tube.com")

        elif "open google" in quarry:
            speak("SURE,sir")
            webbrowser.open("google.com")

        elif "play music" in quarry:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))

        elif 'the time' in quarry:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime},Sir")

        elif "thank you" in quarry:
            speak("it's my pleasure,sir")

        elif "audible" in quarry:
            speak("Yes sir you are,clearly audible")

        elif "hello" in quarry:
            speak("Hello mam ,how are you")

        elif " eat" in quarry:
            speak("I like to eat momos and i love chinese ")

        elif "father" in quarry:
            speak("mister Manthan is my father")

        elif "made" in quarry:
            speak("mister Manthan is my founder")

        elif "your name" in quarry:
            speak("My name is lucifer, i am a inovation of Mister Manthan chouhan")

        elif "you mean" in quarry:
            speak("yes,sir")

        elif "yourself" in quarry:
            speak("okey sir, so.. as you know my name is lucifer and i was born 26th of july in the year 2022,my code is written in python language, mister Manthan chouhan is my founder, he is a student of chemali devi group of institute ")

        elif "ok" in quarry:
            speak("yes,sir")
        elif "open vs code" in quarry:
            codePath = "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe "
            os.startfile(codePath)
        elif "camera" in quarry or "take a photo" in quarry:
            ec.capture(0, "Vica Camera ", "img.jpg")

        elif "restart" in quarry:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in quarry or "sleep" in quarry:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif 'email to manthan' in quarry:
            try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                     speak("Say the subject of the email:")
                     audio = r.listen(source)
                     subject=r.recognize_google(audio)
                     print(f"Subject: {subject}")

                speak("What should I say?")
                content = takeCommand()
                to = "manojchouhan11976@gmail.com"
                sendEmail(to, subject, content)
                speak("Email has been sent!")
  
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")
        elif 'email' in quarry:
            try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                     speak("Say the subject of the email:")
                     audio = r.listen(source)
                     subject=r.recognize_google(audio)
                     print(f"Subject: {subject}")

                speak("What should I say?")
                content = takeCommand()
                to = "ankit.chakrawarti@cdgi.edu.in"
                sendEmail(to, subject, content)
                speak("Email has been sent!")
  
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")
        elif 'mail' in quarry:
            try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                     speak("Say the subject of the email:")
                     audio = r.listen(source)
                     subject=r.recognize_google(audio)
                     print(f"Subject: {subject}")

                speak("What should I say?")
                content = takeCommand()
                to = "shivani.katare@cdgi.edu.com"
                sendEmail(to, subject, content)
                speak("Email has been sent!")
  
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")
        elif 'mail to mitali6' in quarry:
            try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                     speak("Say the subject of the email:")
                     audio = r.listen(source)
                     subject=r.recognize_google(audio)
                     print(f"Subject: {subject}")

                speak("What should I say?")
                content = takeCommand()
                to = "mitalibadole007@gmail.com"
                sendEmail(to, subject, content)
                speak("Email has been sent!")
  
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")
            
        elif "dev CPP editor" in quarry:
            devCpp = "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
            os.startfile(devCpp)
            
        elif "log off" in quarry or "sign out" in quarry:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "update assistant" in quarry:
            speak(
                "After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream=True)

        elif "will you be my gf" in quarry or "will you be my bf" in quarry:
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in quarry:
            speak("I'm fine, glad you me that")

        elif "i love you" in quarry:
            speak("It's hard to understand")

        elif "who am i" in quarry or "who i am" in quarry:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in quarry:
            speak("To serve my Master.")

        elif "change background" in quarry:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "Location of wallpaper", 0)
            speak("Background changed successfully")

        elif 'fine' in quarry or 'good' in quarry:
            speak("It's good to know that you are fine")

        elif "exit" in quarry:
            speak("Thanks for giving me your time, sir")
            exit()

        elif "show my previous" in quarry:
            speak("Opening  your  previous year marksheet,sir")
            power = r"file:///E:/Manthan%20documents/3rd%20sem%20result_.__%20Rajiv%20Gandhi%20Proudyogiki%20Vishwavidyalaya,%20Bhopal%20__._.pdf"
            os.startfile(power)

        elif "machine learning" in quarry:
            speak("Opening  your  machine learning power point presentation,sir")
            ram = r"file:///C:/Users/Asus/Desktop/CS601_Machine%20Learning_Unit%202_Back_Propagation.pdf"
            os.startfile(ram)
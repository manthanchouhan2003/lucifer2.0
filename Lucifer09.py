import subprocess
import pyttsx3
import json
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
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
hiddenimports = [
    'pyttsx3.drivers',
    'pyttsx3.drivers.dummy',
    'pyttsx3.drivers.espeak',
    'pyttsx3.drivers.nsss',
    'pyttsx3.drivers.sapi5', ]

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    print("     ")
    print(f"Lucifer :{audio}")
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir...!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir...!")

    else:
        speak("Good Evening Sir...!")

    assname = ("Vica 1 point o")
    speak("I am lucifer your personal assistent,sir,+-.")
    speak(assname)


def usrname():
    speak("What should I call you sir..!")
    uname = takeCommand()
    speak("Welcome Mister ")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print(" ".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print(" ".center(columns))

    speak("How can I help you , Sir...",)


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizating....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voices.")
        return "None"

    return query

def sendEmail(to, content):
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.ehlo()
   server.starttls()

   server.login('your email id', 'your email password')
   server.sendmail('your email id', to, content)
   server.close()




def command():
    
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching on Wikipedia....')
            query = query.replace("wikipedia", "")
            webbrowser.open("wikkipedia"+query+"")
            # # results = wikipedia.summary(query, sentences=3)
            # speak("According to Wikipedia")
            # print(results)
            # speak(results)

        elif 'open youtube' in query:
            speak("Here you go to YouTube\n")
            webbrowser.open("youtube.com")


        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Hear you go to Stack OverFlow. Happy coding ")
            webbrowser.open("stackoverflow.com")
        # elif 'play music' in query or "play song" in query:
        #     speak("Hear you go with music")
        #     # music_dir = "C:\Users\HP\Videos\movies"
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     random = os.startfile(os.path.join(music_dir, songs[1]))
        elif"play music" in quarry:
            music_dir = 'D:\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[2]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% ")
            speak(f"Sir, the time is {strTime}")

        elif 'open chrome' in query:
            speak("Opening F Drive")
            codePath = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(codePath)

        elif 'open C Drive' in query:
            speak("Opening F Drive")
            codePath = r"This PC\C:"
            os.startfile(codePath)

        elif 'open D Drive' in query:
            speak("Opening F Drive")
            codePath = r"D:"
            os.startfile(codePath)
        elif 'open E Drive' in query:
            speak("Opening F Drive")
            codePath = r"E:"
            os.startfile(codePath)

        elif 'open F Drive' in query:
            speak("Opening F Drive")
            codePath = r"F:"
            os.startfile(codePath)

        # elif 'email to Manthan' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "Receiver email address"
        #         sendEmail(to, content)
        #         speak("Email has been send !")
        #     except Exception as e:
        #         print(e)
        #         speak("I am not able to send this email")

        # elif 'send a mail' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         speak("Whome should I send ?")
        #         to = input()
        #         sendEmail(to, content)
        #         speak("Email has been send !")
        #     except Exception as e:
        #         print(e)
        #         speak("I am not able to send this email")
        elif 'mail to manthan'in query:
            try:
                speak("What should i say")
                content = takeCommand()
                # to = 'technicalmanthan007@gmail.com'"manthan1008"
                sendEmail(to, content) 
                speak("email has been sent.!")
            except Exception as e:
                print(e)
                speak("sorry sir, not able to sent mail please check the mail id")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir..?")

        elif 'fine' in query or 'good' in query:
            speak("It's good to know that you are fine")

        elif "exit" in query:
            speak("Thanks for giving me your time")
            exit()


        elif 'joke' in query:
            webbrowser.open("https://www.rd.com/jokes/")

        elif "calculation" in query:
            # app_id = "Wolframalpha api id"
            # client = wolframalpha.Client(app_id)
            # indx = query.lower().split().index('calculate')
            # query = query.split()[indx + 1:]
            # res = client.query(' '.join(query))
            # answer = next(res.results).text
            # print("The ans is " + answer)
            # speak("The ans is " + answer)
            webbrowser.open("https://www.online-calculator.com/")


        elif "search" in query or "play" in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who am i" in query or "who i am" in query:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in query:
            speak("To serve my Master.")

        elif "power point presentation" in query:
            speak("Opening power point presentation")
            power = r"C:\Users\HP\Downloads\Voice Command Project"
            os.startfile(power)

        elif "SRS report" in query:
            speak("Opening power point presentation")
            power = r"C:\Users\HP\Downloads\Mini Project Report Format_1650089112_1650268384 (1).docx"
            os.startfile(power)

        elif 'what is love' in query:
            speak("Love is the seventh sens which can destroy other six senses.")

        elif "who are you " in query:
            speak("I'm your virtual assistant.")

        elif"reason for you" in query:
            speak("I was created as a Minor Project.")

        elif "change background" in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "Location of wallpaper", 0)
            speak("Background changed successfully")

        elif "thank you" in query:
            speak("it's my pleasure,sir")

        elif "audible" in query:
            speak("Yes sir you are,clearly audible")

        elif "hello" in query:
            speak("Hello mam ,how are you") 

        elif" eat" in query:
            speak("I like to eat momos and i love chinese ")

        elif"father" in query:
            speak("mister Manthan is my father")

        elif"made" in query:
            speak("mister Manthan is my founder")

        elif"your name" in query:
            speak("My name is lucifer, i am a inovation of Mister Manthan chouhan")

        elif"you mean" in query:
            speak("yes,sir")

        elif"yourself" in query:
            speak("okey sir, so.. as you know my name is lucifer and i was born 26th of july in the year 2022,my code is written in python language, mister Manthan chouhan is my founder, he is a student of chemali devi group of institute ")
        
        elif "ok" in query:
            speak("yes,sir")  

        elif "open vs code"in query:
             codePath="C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe "
             os.startfile(codePath)

        elif "dev CPP editor" in query:
            devCpp="C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
            os.startfile(devCpp)


        elif "news" in query:
            # try:
            #     jsonObj = urlopen(
            #         '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
            #     data = json.load(jsonObj)
            #     i = 1
            #
            #     speak('here are some top news from the times of india')
            #     print('''=============== TIMES OF INDIA ============''' + '\n')
            #
            #     for item in data['articles']:
            #         print(str(i) + '. ' + item['title'] + '\n')
            #         print(item['description'] + '\n')
            #         speak(str(i) + '. ' + item['title'] + '\n')
            #         i += 1
            # except Exception as e:
            #
            #     print(str(e))
            webbrowser.open(
                "https://in.search.yahoo.com/yhs/search;_ylt=AwrxgzNeNWVinxIA0zvnHgx.;_ylc=X1MDMjExNDcyMzU1OQRfcgMyBGZyA3locy1mYy0yNDYxBGZyMgNzYi10b3AEZ3ByaWQDeUJ0alJFTmZRY3FvMXdwN04xQVFvQQRuX3JzbHQDMARuX3N1Z2cDMQRvcmlnaW4DaW4uc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAzAEcXN0cmwDMjMEcXVlcnkDVG9wX05ld3NfVG9kYXlfaW5fSW5kaWEEdF9zdG1wAzE2NTA4MDAwNjg-?p=Top_News_Today_in_India&fr2=sb-top&hspart=fc&hsimp=yhs-2461&param1=7&param2=eJwtj0EOgjAQRa8yS01MmbYD2HIMV4awKFCxoVCCGIyndzTu3vszf%2FGH0NdVc7lKRFKG6lMzsxtjzozfE2qplWLpWKRmCAuTIsytQmk1SmUdmtIStdqar7bUe2u6X23wid%2FDzPh0TFN6hxhdlguEwx7mPu0PmDeQKLACDgqq4FXQEdyyRL%2F7dgxblutS6AIO432b4gliGD0MvhvTEbr7miaf8QCBgs6mEFKV8HA3t4Z%2F7wN4qUJE&vm=r&type=fc_ADDA49F0A8D_s58_g_e_d031322_n9998_c13 ")


        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop Vica from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Vica Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "internet speed" in query:
            speak("I am checking it sir....")

        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream=True)

            with open("Voice.py", "wb") as Pypdf:

                total_length = int(r.headers.get('content-length'))

                for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                       expected_size=(total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)

            # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif "Vica" in query:

            wishMe()
            speak("Vica 1 point o in your service Master")
            # speak(assname)

        elif "weather" in query:
            speak("Location")
            # query = query.replace("Indore")
            location = input(query)
            # speak(location)
            # webbrowser.open("https://www.google.nl/weather" + location + "")
            webbrowser.open(
                "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=74f74eee7fd6412237155fe627a5d103")



        # Google Open weather website
            # to get API of Open weather
            # api_key = "Api key"
            # base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            # speak(" City name ")
            # print("City name : ")
            # city_name = takeCommand()
            # complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            # response = requests.get(complete_url)
            # x = response.json()
            #
            # if x["cod"] != "404":
            #     y = x["main"]
            #     current_temperature = y["temp"]
            #     current_pressure = y["pressure"]
            #     current_humidiy = y["humidity"]
            #     z = x["weather"]
            #     weather_description = z[0]["description"]
            #     print(" Temperature (in kelvin unit) = " + str(
            #         current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
            #         current_pressure) + "\n humidity (in percentage) = " + str(
            #         current_humidiy) + "\n description = " + str(weather_description))
            #
            # else:
            #     speak(" City Not Found ")

        elif "send message " in query:
            # You need to create an account on Twilio to use this service
            account_sid = 'Account Sid key'
            auth_token = 'Auth token'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                body=takeCommand(),
                from_='Sender No',
                to='Receiver No'
            )

            print(message.sid)

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "minor project ppt" in query:
            speak("Opening  minor project presentation ppt")
            power = r"C:\Users\HP\Downloads\mps f.ppt"
            os.startfile(power)

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you Mister")
            speak(assname)

            # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif "i love you" in query:
            speak("It's hard to understand")

        elif "what is" in query or "who is" in query:

            # Use the same API key  
            # that we have generated earlier
            # client = wolframalpha.Client("API_ID")
            # res = client.query(query)
            #
            # try:
            #     print(next(res.results).text)
            #     speak(next(res.results).text)
            # except StopIteration:
            #     print("No results")
            query = query.replace("what is", "")
            query = query.replace("who is", "")
            webbrowser.open(query)


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    clear()
    wishMe()
    usrname()
    command()
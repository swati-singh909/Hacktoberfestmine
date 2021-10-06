from platform import uname
import requests
import pyttsx3
import speech_recognition as sr
import datetime
import time
import os
import winshell
import pywhatkit as kit
from pytube import YouTube
from requests import get
import wikipedia
import webbrowser
import subprocess
import subprocess
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import ctypes
import time
import requests





engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

assname = "friday"
def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour >= 0 and hour < 12:
        speak(f"Good Morning sir!,its {tt}  ")

    elif hour >= 12 and hour < 17:
        speak(f"Good Afternoon sir! its  {tt} ")

    else:
        speak(f"Good Evening sir! its {tt} ")

    speak("I am your Assistant")
    speak(assname)



def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception:
        return "none"
    return query

usname = "none"
def username():
    speak("What should i call you sir")
    usname = takecommand()
    speak("Welcome Mister")
    speak(usname)     
    print("====================")
    print("Welcome Mr.", usname)
    print("====================")
     
    speak("How can i Help you, Sir")

class location:  
    res = requests.get('https://ipinfo.io/')
    data = res.json()
    ip = data['ip']
    city = data['city']
    region = data['region']
    country = data['country']
    org = data['org']
    postal = data['postal']
    timezone = data['timezone']

    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]


def calculate(string):
    answer = eval(string)
    return answer

    


if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    username()

    while (True):

        query = takecommand().lower()
        local = location

        # Aplications to run

        if "open notepad" in query:
            speak("openning notepad sir")
            path = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(path)

        elif "open arduino" in query:
            speak("openning arduino sir")
            path = "C:\\Program Files (x86)\\Arduino\\arduino.exe"
            os.startfile(path)

        elif "open command prompt" in query:
            speak("openning command prompt sir")
            os.system("start cmd")

        #  Music Video

        elif "play music" in query or "jarvis play the music" in query or "play the music" in query or "Jarvis play music" in query:
            speak("Yeah sure but what you want to listen sir?")
            pp = takecommand().lower()
            kit.playonyt(pp)

        # Operations
        elif "wikipedia" in query:
            speak("searching in wikipedia sir....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("sir according to wikipedia")
            speak(results)

        elif "where am i" in query or "location" in query or "where i am" in query:
            speak("let me find sir")
            speak(f"I guess sir we are in {local.city} city in {local.country}")
            speak("Should i find more details")
            tt = takecommand().lower()
            if "yes" in tt or "yep" in tt or "yeah" in tt:
                print("Latitude : ", local.latitude)
                print("Longitude : ", local.longitude)
                print("IP : ", local.ip)
                print("City : ", local.city)
                print("Region : ", local.region)
                print("Country : ", local.country)
                print("Org : ", local.org)
                print("Postal : ", local.postal)
                print("Timezone : ",local.timezone)


        elif "time" in query:
            timee = time.strftime("%I:%M %p")
            speak(f"Sir its {timee}")
            
 
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            usname = query
            speak("Name changed")
 
        elif "change your name" in query:
            speak("What would you like to call me, Sir ")
            assname = takecommand()
            speak("Thanks for naming me")
 
        elif "what's your name" in query or "what is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
 
        elif 'exit' in query or 'quit' in query:
            speak("Thanks for using me")
            exit()
 
        elif 'joke' in query:
            speak(pyjokes.get_joke())
    
            
        elif "who i am" in query:
            speak("I guess if you talk then definitely you are a human.")
 
            
        elif "who made you" in query or "who created you" in query:
            speak("I was created as a Minor project by Mister Ayush in 2019,, as a attempt to help users who are blind or want to perform task using assistant")
        
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
 
        elif "who are you" in query:
            speak("I am your virtual assistant created by Mister, Ayush")
 
 
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
            note = takecommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takecommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime =time.strftime("%I:%M %p")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            for lines in file:
                speak(lines)

        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
 
        elif 'shutdown' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                 
        elif f"{assname}" in query:
            speak(f"{assname} in your service Mister")
            speak(usname)  
                 
        elif 'empty recycle bin' in query or 'empty recyclebin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
 
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time in seconds you want me to  stop listening")
            try:
                a = int(takecommand())
                time.sleep(a)
                print(a)
            except Exception as e:
                print("Give time in seconds eg-> 10")

        elif "good morning" in query:
            speak("A warm" +query)
            speak("How are you Mister")
            speak(usname)
        
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
 
        elif "will you be my gf" in query:  
            speak("I'm not sure about that, may be you should give me some time")
 
        elif "how are you" in query:
            speak("I'm fine, glad you ask that")
 
        elif "i love you" in query:
            speak("not more than i do")
        
        elif "calculate" in query:
            speak(" Yeah sure tell the equation")
            cal = takecommand()
            try:           
                answer = calculate(cal)  
                speak("The answer is " + str(answer))
            except Exception as e:
                print(" Sorry can't understand try again")
                
        elif "youtube" in query:
            webbrowser.open_new_tab("www.youtube.com")

        elif "news" in query:
            speak("showing latest news sir")
            webbrowser.open("latest news")
        
        elif "instagram" in query:
            speak("sure sir")
            webbrowser.open_new_tab("www.instagram.com")

        elif "google" in query:
            speak("sir, what should i search on google")
            num = takecommand().lower()
            webbrowser.open(f"{num}")

        elif "stackoverflow" in query:
            webbrowser.open_new("www.stackoverflow.com")

        elif "blogger" in query:
            webbrowser.open_new_tab("www.blogger.com")

        elif "play" in query:
            speak("yeah sure sir")
            query = query.replace("youtube", "")
            kit.playonyt(query)
        
        
        elif "ip" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")


        elif query == "none":
            continue

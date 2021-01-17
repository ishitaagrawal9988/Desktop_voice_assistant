import pyttsx3
from random import randint
import speech_recognition as sr               #pip install pipwin     pipwin install pyaudio
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
#print(voices[1].id)
engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am jarvis. How may i help you")

def takeCommand():
    #it take microphone input from the user and return string
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognizing...")
        query=r.recognize_google(audio)#, 'Language'="en-in") #english india
        print(f"user said: {query}\n")
    except Exception as e :
        print(e)
        print("say it again please")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("email-id","password")
    server.sendmail("email-id",to,content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        query=takeCommand().lower()
        #login for excecuting task based on query
        if "jarvis" in query:
            if 'wikipedia' in query:
                speak("Searching wikipedia...")
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif "open youtube" in query:
                webbrowser.open("youtube.com")
            elif "open google" in query:
                webbrowser.open("google.com")
            elif "open stack overflow" in query:
                webbrowser.open("stackoverflow.com")
            elif "open music" in query:
                rand=randint(0,14)
                music_dir="D:\\music"
                songs=os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[rand]))
            elif "time" in query:
                strtime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strtime}")

            elif "open code" in query:
                codepath="C:\\Users\\hp\\AppData\\Local\\atom\\atom.exe"
                os.startfile(codepath)

            elif "send email" in query:
                try:
                    speak("What should i say?")
                    content=takeCommand()
                    to="email-id"
                    sendEmail(to,content)
                    speak("Email has been send successfully")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend, i am not able to send email")


            elif "stop" in query:
                exit()

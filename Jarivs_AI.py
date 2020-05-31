import pyttsx3 as p
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import sys

engine=p.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Hi,Good Morning')
    elif hour>=12 and hour<=18:
        speak('Good AfterNoon')
    else:
        speak('Good Evening')
    speak('Hi, This is Anshu Mishra, How may i help you!')
    
def take():
    r=sr.Recognizer()
    with sr.Microphone() as Source:
        print("Listing....")
        r.pause_threshold=1
        audio=r.listen(Source)
    
        try:
            query=r.recognize_google(audio)
            print('User Said:{}'.format(query))
        except:
            print("Please Say Again")
            return "None"
    return query        
 
if __name__ == "__main__":
    wish()
    while True:
        query=take().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query=query.replace("wikipeida","")
            results=wikipedia.summary(query,sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            print('Opening Youtube...')
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            print('Opening Google...')
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            print('Opening Stack Overflow...')
            webbrowser.open("youtube.com")
        elif 'open Facebook' in query:
            print('Opening Facebook')
            webbrowser.open("facebook.com")
        elif 'play music' in query:
            print('Looking for your Favorites')
            music_dir= 'F:\Music_dir'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'time' in query:
            t=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the Time is{t}")
        elif 'open chrome' in query:
            path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
        elif 'open keep' in query:
            kep="https://keep.google.com/u/0/#home"
            os.startfile(kep) 
        elif 'exit' in query:
            exit()
                 
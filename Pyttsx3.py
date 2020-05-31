import pyttsx3 as p
import datetime
import speech_recognition as sr



engine=p.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour<=0 and hour>=12:
        speak('Hi,Good Morning')
    elif hour>12 and hour<=18:
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
            text=r.recognize_google(audio)
            print('User Said:{}'.format(text))
        except:
            print("Please Say Again")
            return "None"
    return text        
 
if __name__ == "__main__":
    wish()
    query=take()
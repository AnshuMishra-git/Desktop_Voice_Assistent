import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as Source:
    print("Listing....")
    r.pause_threshold=1
    audio=r.listen(Source)
    
    try:
        text=r.recognize_google(audio)
        print('You Said:{}'.format(text))
    except:
        print("Sorry Unale to Recognize")
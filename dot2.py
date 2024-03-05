import pyttsx3
import speech_recognition as sr
import datetime 
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!") 

    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am DOT sir, How may I help you")

def takecommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.... ")
        r.pause_threshold = 1 # second of non-audio before a phrase is considered complete
        audio = r.listen(source)

        try:
            print("Recognizing..")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please ...")
            return "None" 
        return query    
def sendEmail(to,content):
     server = smtplib.SMTP('smtp.gmail.com', 587)
     server.ehlo()
     server.starttls()
     server.login('harshmanhas203@gmail.com','sheetal11980')
     server.sendmail('harshmanhas203@gmail.com',to,content)
     server.close()

    

if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak ('searching wkipedia...')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2) #sentences means red no. of line on wikipedia
            speak("According to Wikipedia")
            print(results)
            speak(results)
            #  browser action add .com or links to open sites like
        elif'open youtube' in query:
            webbrowser.open("youtube.com")
        elif'open google' in query:
            webbrowser.open('google.com')    
        elif'open facebook' in query:
            webbrowser.open('facebook.com')     
        elif'open instagram' in query:
            webbrowser.open('instagram.com') 
        elif'open whatsapp' in query:
            webbrowser.open('whatsapp.com')  

        elif'play music' in query:
            music_dir = 'C:\\Users\\Lenovo\\Music\\Playlists'    
            songs = os.listdir(music_dir)
            random.shuffle(songs)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))  

        elif'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")   

       # elif'open code' in query:
         #   codePath"C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         #   os.startfile(codePath)   #
        elif 'email to navi' in query:
            try:
                speak("what should i say?") 
                content = takecommand ()
                to ="harshmanhas203@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir i am not able to send this email ")
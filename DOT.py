import pyttsx3
import speech_recognition as sr
import datetime 
import wikipedia

engin = pyttsx3.init('sapi5')
voices = engin.getProperty('voices')
#print(voices[1].id)
engin.setProperty('voice',voices[1].id)


def speak(audio):
    engin.say(audio)
    engin.runAndWait()
def wishMe():
   hour = int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:
      speak("Good Morning!") 

   elif hour>=12 and hour<18:
       speak("Good Afternoon")
   else:
       speak("good evening")


   speak("I am DOT sir, How may i help you")
   
def takecommand():
      #it take microphone input from the user and return string output

      r = sr.Recognizer()
      with sr. microphone() as source:
         print("listening.... ")
         r.pause_threshold = 1# second of non audio before a phase is consider complete
         audio = r.listen(source)

         try:
            print("Recognizing..")
            query = r.recognize_google(audio,Language='en-in')
            print(f"user said: {query}\n")

         except Exception as e:
            #print(e)
            print("say that again please ...")
            return "None" 
         return query    

if __name__ == "__main__":
   wishMe()
   while True:
     query = takecommand().lower()
   if'wikipedia' in querry: #logic for executing tasks base on querry
         query = query.replace("wikipedia","")
         results =wikipedia.summary(query,sentences=2)
         speak("according to wikipedia")
         print(results)
         speak(results)
   





    
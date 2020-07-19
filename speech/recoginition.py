import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
   engine.say(audio)
   engine.runAndWait()
def wishMe():
       hour=int(datetime.datetime.now().hour)
       if hour>=0 and hour<12:
              speak("Good Morning")
       elif hour>=12 and hour<=18:
             speak("Good Afternoon")
       else:
             speak("Good Evening")
       speak(" hello sir, i am jarvis, how may i help you")

def takeCommand():
   # it takes microphone input from the user and return string output
   r=sr.Recognizer()
   with sr.Microphone() as source:
      print("Listening....")
      r.pause_threshold=1
      audio=r.listen(source)
   try:
      print("Recognizing...")
      query=r.recognize_google(audio,language='en-in')
      print(f"user said:{query}")
   except Exception as e:
      # print(e)
      print("Say that again please...")
      query=None
   return query 
def sendEmail(to,content):
       server=smtplib.SMTP('smtp.gmail.com',587)
       server.ehlo()
       server.starttls()
       server.login("rohanmahto592@gmail.com","Rohan1234.$")
       server.sendmail("kailashmahto735185@gmail.com",to,content)
       server.close()





if _name_ == "_main_":
   wishMe()
   query=takeCommand()
   ## logic for exequting basic tas
   if 'wikipedia' in query.lower():
          speak("searching wikipedia....")
          query=query.replace("wikipedia","")
          results=wikipedia.summary(query, sentences= 2)
          print(results)
          speak(results)
   elif "open youtube" in query.lower():
      #webbrowser.open("youtube.com")
          url="youtube.com"
          chrome_path='C:/Program Files (x86)/Google/Chrome/Application/Chrome.exe %s'
          webbrowser.get(chrome_path).open(url)
   elif "open google" in query.lower():
          url="google.com"
          chrome_path='C:/Program Files (x86)/Google/Chrome/Application/Chrome.exe %s'
          webbrowser.get(chrome_path).open(url)
   elif "open stackoverflow" in query.lower():
          url="stackoverflow.com"
          chrome_path='C:/Program Files (x86)/Google/Chrome/Application/Chrome.exe %s'
          webbrowser.get(chrome_path).open(url)
   elif "open facebook" in query.lower():
          url="facebook.com"
          chrome_path='C:/Program Files (x86)/Google/Chrome/Application/Chrome.exe %s'
          webbrowser.get(chrome_path).open(url)
   elif "open instagram" in query.lower():
          url="instagram.com"
          chrome_path='C:/Program Files (x86)/Google/Chrome/Application/Chrome.exe %s'
          webbrowser.get(chrome_path).open(url)
   elif "play music" in query.lower():
          songs_dir="C:\\Users\\Komal\\Music"
          songs=os.listdir(songs_dir)
          print(songs)
          os.startfile(os.path.join(songs_dir,songs[1]))
   elif " the time" in query.lower():
          strtime=datetime.datetime.now().strftime("%H:%M:%S")
          speak(f" the time is  {strtime}")
   elif " open whatsapp" in query.lower():
          codepath="C:\\Users\\Komal\\AppData\\Local\\WhatsApp"
          os.startfile(codepath)
   elif ' send email to kailash' in query.lower():
          try:
             speak("what should i send")
             content=takeCommand()
             to="kailashmahto735185@gmail.com"
             sendEmail(to,content)
             speak("email has been sent succesfully")
          except Exception as e:
             print(e)
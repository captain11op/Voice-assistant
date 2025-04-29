import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         recognizer.adjust_for_ambient_noise(source)
         audio = recognizer.listen(source)
         try:
              print("Recognizing. . .")
              data = recognizer.recognize_google(audio)
              print(data)
              return data 
         except sr.UnknownValueError:
              print("Please repeat again")

def texttospeech(x):
     engine = pyttsx3.init()
     voices = engine.getProperty('voices')
     engine.setProperty('voice',voices[0].id)
     engine.getProperty('rate')
     speed = engine.setProperty('rate',110)
     engine.say(x)
     engine.runAndWait()

if __name__ == '__main__':
     
     data = sptext().lower()
     if "peter" in data.lower():
         while True:
          data1 = data1.lower()
          
          if "name" in data1:
                    name = "My name is peter"
                    texttospeech(name)
          elif "old" in data1:
                    old = "I am 1 day old "
                    texttospeech(old)
          elif "age" in data1:
                    age =  "i am 1 day old"
                    texttospeech(age)
          elif "time" in data1:
                    time = datetime.datetime.now().strftime("%I%M%p")
                    texttospeech(time)
          elif "date" in data1:
                    date = datetime.date.today()
                    texttospeech(date)
          elif "google" in data1:
                    webbrowser.open("https://www.google.com")
                    google = "Google opened"
                    texttospeech(google)
          elif "youtube" in data1:
                    webbrowser.open("https://www.youtube.com")
                    youtube = "Youtube opened"
                    texttospeech(youtube)
          elif "facebook" in data1:
                    webbrowser.open("https://www.facebook.com")
                    facebook = "Facebook opened"
                    texttospeech(facebook)
          elif "instagram" in data1:
                    webbrowser.open("https://www.facebook.com")
                    instagram = "Instagram opened"
                    texttospeech(instagram)
          elif "x" in data1:
                    webbrowser.open("https://www.x.com")
                    X = "X opened"
                    texttospeech(X)
          elif "chatgpt" in data1:
                    webbrowser.open("https://www.chat.openai.com")
                    chatgpt = "chatgpt opened"
                    texttospeech(chatgpt)
          elif "whatsapp" in data1:
                    webbrowser.open("https://www.whatsapp.com")
                    whatsapp = "whatsapp opened"
                    texttospeech(whatsapp) 
          elif "wikipedia" in data1:
                    webbrowser.open("https://www.wikipedia.org")
                    wikipedia = "wikipedia opened"
                    texttospeech(wikipedia) 
          elif "reddit" in data1:
                    webbrowser.open("https://www.reddit.com")
                    reddit = "reddit opened"
                    texttospeech(reddit) 
          elif "amazon" in data1:
                    webbrowser.open("https://www.amazon.com")
                    amazon = "amazon opened"
                    texttospeech(amazon) 
          elif "netflix" in data1:
                    webbrowser.open("https://www.netflix.com")
                    netflix = "netflix opened"
                    texttospeech(netflix) 
          elif "linkedin" in data1:
                    webbrowser.open("https://www.linkedin.com")
                    linkedin = "linkedin opened"
                    texttospeech(linkedin) 
          elif "microsoft 365" in data1:
                    webbrowser.open("https://www.office.com")
                    micro365 = "micrsoft 365 opened"
                    texttospeech(micro365) 
          elif "pinterest" in data1:
                    webbrowser.open("https://www.pinterest.com")
                    pinterest = "pinterest opened"
                    texttospeech(pinterest) 
          elif "microsoft" in data1:
                    webbrowser.open("https://www.microsoft.com")
                    microsoft = "microsoft opened"
                    texttospeech(microsoft) 
          elif "twitch" in data1:
                    webbrowser.open("https://www.twitch.tv")
                    twitch = "twitch opened"
                    texttospeech(twitch) 
          elif "joke" in data1:
                    joke_1 = pyjokes.get_joke(language="en",category="all")  
                    texttospeech(joke_1)
          elif "github" in data1:
                    webbrowser.open("https://github.com") 
                    github = "github opened"
                    texttospeech(github)
          elif "exit" in data1:
                  thx = "Thank you for using me go check out my owner captain11op github. he got many other projects too"
                  texttospeech(thx)
                  break
          time.sleep(2)
     else:
        print("Please repeat and my name is peter call me peter")
     


              
        
        















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































                                          


                                            
import pyttsx3 # text to speech
import datetime
import speech_recognition as sr # speech to text
import smtplib 
from secrets import senderemail,epwd,to
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit as kit
import requests # to request data fromt the api
from newsapi import NewsApiClient
import clipboard # this will read the text whatever you point to__...
import os
import pyjokes
import time as tt
import string
import random
import psutil

engine = pyttsx3.init()

# TODO: speak the audio whatever capture from the mic
def speak(audio):
     engine.say(audio)
     engine.runAndWait()

# TODO: male voice and female voice
def getvoices(voice):
     voices = engine.getProperty("voices")
     # print(voice[1].id)
     if voice ==1:
          engine.setProperty("voice", voices[0].id)
          speak("Jarvis here!")
     if voice ==2:
          engine.setProperty("voice", voices[1].id)
          speak("Friday here!")
     
     
# TODO:  get the  current time    
def time():
     speak('The current time is')
     Time = datetime.datetime.now().strftime("%I:%M:%S")  # give us the current time and store it in the Time
     speak(Time) 

# get the current time
def date():
     #store the year , month and date respectively
     speak('The current date is')
     year = int(datetime.datetime.now().year) 
     month = int(datetime.datetime.now().month)
     date = int(datetime.datetime.now().day)
     speak(date)
     speak(month)
     speak(year)
# wishme
def wishme():
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
        speak("Good Morning!")

     elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

     else:
        speak("Good Evening!")  

     speak("I am Jarvis Sir. Please tell me how may I help you")    

# greet mee
# def greeting():
#      hour = int(datetime.datetime.now().hour)
#      if hour >= 6 and hour <12:
#           speak("Good Morning Sir")
#      elif hour >= 12 and  hour <18:
#           speak('Good Afternoon Sir')
#      elif hour >= 18 and hour <24:
#           speak('Good Evening Sir')
#      else:
#           speak('Good Night Sir')

# # wish me
# def wishme():
#      speak('Welcome Back Sir!')
#      time()
#      date()
#      greeting()
#      speak('Jarvis at your service. please tell me how can i help you?')
# take request through mic
def takeCommandMic():
     r = sr.Recognizer()
     with sr.Microphone() as source: # listen with the microphone what we speak as a source
          print("Listenning......")
          r.pause_threshold = 1 # wait for 1sec and then start listening
          audio = r.listen(source)  # this contain what we spoke
     try:
          print('Recognizing.....')
          query = r.recognize_google(audio, language = 'en-in') #this query contain all the data this is listen 
          print(query)
     except Exception as e:
          print(e)
          speak("Say that again Please")
          return "none"
          

     return query
# take request from CMD
def takeCommandCMD():
     query = input("Please tell me how can i help you?")
     return query

# send email
def sendEmail(receiver,subject,content):
     server = smtplib.SMTP('smtp.gmail.com',587)
     # transport layer security (TLS)
     server.starttls()
     server.login(senderemail, epwd)
     email = EmailMessage()
     email['From'] = senderemail
     email['To'] = receiver
     email['Subject'] = subject
     email.set_content(content)
     server.send_message(email)
     print('Email sent successfully.....')
     server.close()

# send WhatsAppMessage
def sendWhatsAppMessage(phone_no,message):
     Message = message
     wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
     sleep(10)
     pyautogui.press('enter')

# take command form the user and search it in the google
def searchgoogle():
     speak("what should i search for??")
     search = takeCommandMic()
     wb.open('https://www.google.com/search?q='+search)

def news():
     newsapi = NewsApiClient(api_key='e18cd1eb978840efacab7d41a57874fd')
     speak(("What topic you need the news about?"))
     topic = takeCommandMic()
     data = newsapi.get_top_headlines(q=topic,language='en',page_size=5)
     newsdata = data['articles']
     for x,y in enumerate(newsdata):
          print(f'{x}{y["description"]}')
          speak((f'{x}{y["description"]}'))
     speak("That's it for now i'ill update you in some time")

# convert text to speech
def text_to_speech():
     text = clipboard.paste()
     print(text)
     speak(text)

# get the covid data
def covid():
     r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
     data = r.json() 
     covid_data = f'Confirmed cases : {data["cases"]} \n Deathes : {data["deathes"]} \n Recoverd cases : {data["revoverd"]} '
     print(covid_data)
     speak(covid_data)

# screenshot code
def screenshot():
     name_img = tt.time()
     name_img = f'C:\\Users\\91996\\Desktop\\Projects\\Python Projects\\JARVIS\\screenshot\\{name_img}.png'
     img = pyautogui.screenshot(img_name)
     img.show()

# generate password
def passwordgen():
     s1 = string.ascii_uppercase 
     s2 = string.ascii_lowercase 
     s3 = string.digits
     s4 = string.punctuation

     passlen = 8
     s = []
     s.extend(list(s1))
     s.extend(list(s2))
     s.extend(list(s3))

     random.shuffle(s)
     newpass = (''.join(s[0:passlen])) # this will generate some passwords
     print(newpass)
     speak(newpass)

# cpu temperature
def cpu():
     usage = str(psutil.cpu_percent())
     speak("CPU is at "+usage)
     battery = psutil.sensors_battery()
     speak(f"Battery is at {battery.percent} % ")
  
     
     
# Flip a clon for me
def flip():
     speak("Okay sir , flipping a coin")
     coin = ['heads', 'tails']
     toss = []
     toss.extend(coin)
     random.shuffle(toss)
     toss = (''.join(toss[0]))
     speak("I flipped the coin and you got"+ toss)

# roll a dice
def roll():
     speak("Rolling a die for you")
     die = ['1','2','3','4','5','6']
     roll = []
     roll.extend(die)
     random.shuffle(roll)
     roll = (''.join(roll))
     print(roll)
     speak("I rolled a die and you got" + roll)
     

# TODO: MAIN FUNCTION
if __name__ == '__main__':
     getvoices(1) # switch bettwen 1 and 2 male and female
     wishme()
     while True:
          query = takeCommandMic().lower()
          if "time" in query:
               time()
          elif 'date' in query:
               date()
          elif 'email' in query:
               email_list = {
                    'test email':'demoacc1011@gmail.com'
               }
               try:
                    speak("To whom you want to send the mail?")
                    name = takeCommandMic()
                    receiver = email_list[name]
                    speak("What is the subject of the mail?")
                    subject = takeCommandMic()
                    speak("What should i say?")
                    content = takeCommandMic()
                    sendEmail(receiver,subject,content)
                    speak("Email has been send")
               except Exception as e:
                    print(e)
                    speak(" Sorry unable to send the email")
          elif 'message' in query:
               user_name = {
                    'Jarvis' : '+91 76205 59721'
               }
               try:
                    speak("To whom you want to send the whatsapp message?")
                    name = takeCommandMic()
                    phone_no = user_name[name]
                    speak("What is the message?")
                    message = takeCommandMic()
                    sendWhatsAppMessage(phone_no,message)
                    speak("Message has been send")
               except Exception as e:
                    print(e)
                    speak(" Sorry unable to send the WhatsAppMessage")             

          elif 'wikipedia' in query:

               speak("Searching Wikipedia...")
               query = query.replace("Wikipedia", "")
               results = wikipedia.summary(query , sentences=2)
               speak("According to Wikipedia")
               print(results)
               speak(results)    

          
          elif 'search' in query:
               searchgoogle()

          elif "youtube" in query:
               speak("What should i search for? on youtube")
               topic = takeCommandMic()
               kit.playonyt(topic) #imported from the library


          elif 'weather' in query:
               city = 'mumbai'
               url ='https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=2ffed89c14ec6fa6f7fa8e3f475d84cd' 
               res = requests.get(url) # will stroe the jason data 
               data = res.json()
               # now we have the data and now we can acess the data from the API_KEY
               weather = data['weather'][0]['main']
               temp = data['main']['temp']
               description = data['weather'][0]['description']
               # converting farenight to the degrees
               temp = round((temp -32)*5/9)
               print(weather)
               print(temp)
               print(description)
               speak(f'weather in {city} city is like')
               speak(f'Temperature is :{temp} degrees celsius')
               speak(f'Weather is :{weather} ')
              
          elif 'news' in query:
               news()
          
          elif 'read' in query:
               text_to_speech()

          elif 'covid' in query:
               covid() 

          elif "open my document" in query:
               os.system('explorer C://{}'.format(query.replace('Open','')))

          
          elif 'open code' in query:
               code_path = 'C:\\Users\\91996\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
               os.startfile(code_path)

          elif 'open google' in query:
                wb.open("google.com")

          elif 'stack overflow' in query:
               wb.open("stackoverflow.com")   

          elif 'joke' in query:
               print(pyjokes.get_joke())
               speak(pyjokes.get_joke())
               # speak(pyjokes.get__joke())
               speak("hahahahahahahahahahahah")

          elif 'screenshot' in query:
               screenshot()

          elif 'remember that' in query:
               speak("What should i remember?")
               data = takeCommandMic()
               speak("you said me to remember that "+ data)
               remember = open("data.txt",'w')
               remember.write(data)
               remember.close()

          elif 'do you know anything' in query:
               remember = open("data.txt",'r')
               speak(f'you told me to remember that {remember}')

          elif 'passwords' in query:
               passwordgen()

          elif 'flip' in query:
               flip()

          elif "roll" in query:
               roll()

          elif "cpu" in query:
               cpu()

          elif 'offline' in query:
               quit()   



          

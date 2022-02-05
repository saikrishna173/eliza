import speech_recognition as sr
import os
import sys
import re
import os
import pyautogui
import webbrowser
from datetime import date
import smtplib
import requests
import subprocess
import pyttsx3
from pyowm import OWM
import youtube_dl
import webbrowser  
from GoogleNews import GoogleNews
import pywhatkit
def note(text):
    file_name = "eleesa notepad writings" +"-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])
import urllib
import requests 
from datetime import datetime
import json
from bs4 import BeautifulSoup as soup
import json
from difflib import get_close_matches as match
import pyjokes




import wikipedia
import random
from time import strftime


listner=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)



def elisaResponse(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    with sr.Microphone() as source:
        print("listening....")
        listner.adjust_for_ambient_noise(source)
        voice=listner.listen(source)
        global command 
        command=listner.recognize_google(voice)
        command=command.lower()
        if "eleesa"in command:
            command=command.replace("eleesa","")        
            
        return command
def assistant():
    
    command=take_command()
    if 'shutdown' in command:
        elisaResponse('Bye bye Sir. Have a nice day')
        sys.exit()

    #open website
    elif 'open' in command:
        reg_ex = re.search('open (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            print(domain)
            url = 'https://www.' + domain+'.com'
            webbrowser.open(url)
            elisaResponse('The website you have requested has been opened for you Sir.')
        else:
            pass
   
    elif 'introduce yourself' in command:
        elisaResponse('hi, i am eleesa you virtual personal assistant , i was born on the nineteenth of january twenty twenty two,MASTER SAI KRISHNA created me')
    #greetings
    
    elif 'hello' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            elisaResponse('Hello Sir. Good morning')
        elif 12 <= day_time < 18:
            elisaResponse('Hello Sir. Good afternoon')
        else:
            elisaResponse('Hello Sir. Good evening')
    
    elif 'hi' in command:
        elisaResponse("hi sir ,it is great to talk to you ")
    
    elif 'thank you' in command:
        elisaResponse("glad i can help")
    
    elif 'very good' in command:
        elisaResponse("thank you for the compliment sir")
    
    elif 'how are you'in command:
        elisaResponse("i am fine and ready to help you sir ")
    
    elif 'what can you do' in command:
        elisaResponse("""
        You can use these commands and I'll help you out:
        1. Open example.com : replace example with any website name
        2. Send email : Follow up questions such as recipient name, content will be asked in order.
        3. Tell a joke : Says a random joke.
        4. Greetings
        5. play me a example song  : Plays song in your youtube 
        6. news for today : displays top news of today
        7. time : Current system time
        8. tell me about anything : tells you about anything
        9.where is example:opens an shows you location on google map
        10. current temperature:it will respond with current temprature
        11. elisa can also take voice commanded screenshot
        12.shows you the current weather
        13.will it rain todday shows precipitation rate
        14.show me the weekly forecast
        15.date and time
        16 introducing herself
        17.you can also share your feedback for that simply say i have a feedback
        """)
    #top stories from google news
    elif 'news for today' in command:
        elisaResponse("opening the top stories from google")
        newsurl='https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en'
        webbrowser. open(newsurl)

    elif "where is" in command:
        location = command.replace("where is ","")
        elisaResponse("I will show you where " + location + " is.")
        mapurl='https://www.google.nl/maps/place/' + location + '/&amp;'
        webbrowser. open(mapurl)
    
    elif "will it rain today " in command :
        sofiaResponse("opening the weather forecast on google weather ")
        weatherForecasturl='https://www.google.com/search?q=google+weather&rlz=1C1VDKB_enIN988IN988&oq=g&aqs=chrome.0.69i59l2j46i67i131i199i433i465j69i57j69i60l4.2250j0j7&sourceid=chrome&ie=UTF-8'
        webbrowser. open(weatherForecasturl)

    elif "show me the weakly forecast " in command :
        elisaResponse("opening the weekly weather forecast on google weather ")
        forecasturl='https://www.google.com/search?q=google+weather&rlz=1C1VDKB_enIN988IN988&oq=g&aqs=chrome.0.69i59l2j46i67i131i199i433i465j69i57j69i60l4.2250j0j7&sourceid=chrome&ie=UTF-8'
        webbrowser. open(forecasturl)
    #time
    elif "are  you living " in command:
        sofiaResponse("i am not living in physical state i live in the cloud")

    elif 'time' in command:
        import datetime
        now = datetime.datetime.now() 
        elisaResponse('Current time is %d hours %d minutes' % (now.hour, now.minute))
    
    #send email
    elif 'send email to dad' in command:
        recipient = 'sundarmani99@gmail.com'
        if  recipient:
            elisaResponse('What should I say to him?')
            content = take_command()
            print("YOU SAID"+content)
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login('saikrishckn@gmail.com', 'saikrish143(')
            mail.sendmail('saikrishckn@gmail.com','sundarmani99@gmail.com', content)
            mail.close()
            elisaResponse('Email has been sent successfuly. You can check your inbox.')
        else:
            elisaResponse('I don/t know what you mean!')

    elif 'screenshot' in command:
        image = pyautogui.screenshot()
        image.save('screenshot.png')
        elisaResponse('Screenshot taken.')

    #ask me anything
    elif 'tell me about' in command:
        person=command.replace("tell me about ","")
        info=wikipedia.summary(person, 1)
        print(info)
        elisaResponse(info)
    
    elif "play" in command:
        song=command.replace("play","")
        elisaResponse("playing "+song)
        pywhatkit.playonyt(song)
        
    elif "who is" in command:
        person=command.replace("who is ","")
        info=wikipedia.summary(person, 1)
        print(info)
        elisaResponse(info)
    
    elif "who created you" in command:
        elisaResponse("MASTER SAI KRISHNA ")
    
    
    elif "tell me a story" in command:
        elisaResponse("here is a short story")
        Sentence_starter = ['About 100 years ago', ' In the 20 BC', 'Once upon a time']
        character = [' there lived a king.',' there was a man named Jack.',' there lived a farmer.']
        once = [' One day', ' One full-moon night']
        story_plot = [' he was passing by',' he was going for a picnic to ']
        place = [' the mountains', ' the garden']
        second_character = [' he saw a man', ' he saw a young lady']
        age = [' who seemed to be in late 20s', ' who seemed very old and feeble']
        work = [' searching something.', ' digging a well on roadside.']
        elisaResponse(random.choice(Sentence_starter)+random.choice(character)+
      random.choice(once)+random.choice(story_plot) +
      random.choice(place)+random.choice(second_character)+
      random.choice(age)+random.choice(work))
    
    elif "tell me a joke" in command:
        elisaResponse(pyjokes.get_joke())

    elif 'tell me the current weather' in command:
        search='temperature in chennai'
        weatherurl= f"https://www.google.com/search?q={search}"
        varr= requests.get(weatherurl)
        data=soup(varr.text,"html.parser")
        temp=data.find("div",class_="BNeawe").text
        elisaResponse(f"current{search} is {temp} ")
    
    elif 'date' in command:
      today = date.today() 
      print("it is",today.day,today.month,today.year)
    
    elif 'write it down' in command:
        elisaResponse("What would you like me to write down? ")
        write_down = take_command()
        note(write_down)
        elisaResponse("I've made a note of that.")
        

    elif 'you are a waste' in command:
        recipient = 'saikrishckn@gmail.com'
        if  recipient:
            elisaResponse('please say your feedback so that i can improve:')
            content = take_command()
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login('saikrishckn@gmail.com', 'saikrish143(')
            mail.sendmail('sundarmani99@gmail.com','saikrishckn@gmail.com', content)
            mail.close()
            elisaResponse('your feedback has been recorded successfuly i will improve that.')

        elif 'i have a feedback' in command:
         recipient = 'saikrishckn@gmail.com'
         if  recipient:
            elisaResponse('please say your feedback so that i can improve:')
            content = take_command()
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login('saikrishckn@gmail.com', 'saikrish143(')
            mail.sendmail('sundarmani99@gmail.com','saikrishckn@gmail.com', content)
            mail.close()
            elisaResponse('your feedback has been recorded successfuly i will improve that.')
         else:
            elisaResponse('I don/t know what you mean!')
    elif "what is my name" in command:
        elisaResponse("your name is sai krishna sundarrajan")
    elif "what is my mother's name" in command:
     elisaResponse("your mothers name is thamizh selvi sundarrajan")
    elif "what is my father's name" in command:
            elisaResponse("your fathres name is sundarrajan mani")
    elif "where do i live"in command:
        elisaResponse("you live in chennai,tamil nadu")
    elif "when is your birthday"  in command:
        elisaResponse("i was born on the nineteenth of january twenty twenty two")
    else:
      elisaResponse("please say that again")
while True:
    assistant()
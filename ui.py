from email import message
import pyttsx3
import datetime
import speech_recognition as sr
import screen_brightness_control as pct
import smtplib
from secret import senderemail, pas, tp
from email.message import EmailMessage
import pyautogui
import webbrowser as web
from time import sleep
import wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes

import time as tt
from googletrans import Translator
from google_trans_new import google_translator


recognizer = sr.Recognizer()
engine = pyttsx3.init()

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    newVoiceRate = 145
    engine.setProperty('rate', newVoiceRate)


def getvoices(voice):
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
    if voice == 2:
        engine.setProperty('voice', voices[1].id)
    speak("hello this is sylex")


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is:")
    speak(Time)


def date():
    yr = int(datetime.datetime.now().year)
    mon = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(yr)
    speak(mon)
    speak(day)


def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("good afternoon")
    elif hour >= 18 and hour < 24:
        speak("good evening")
    else:
        speak("good night")


def wishme():
    speak("Welcome")

    greeting()
    speak("sylex is at your service")


def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("say that again please...")
        return "None"
    return query


def sendEmail(tp, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderemail, pas)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = tp
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()


def sendwhatsapp(pho_no, message):
    Message = message
    web.open('https://web.whatsapp.com/send?phone='+pho_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')


def screenbright():
    speak("tell the persentage of brightness you want in numbers")
    level = takeCommandMic()
    pct.set_brightness(level)


def searchongoogle():
    speak("what should i search for ?")
    search = takeCommandMic()
    web.open('https://www.google.com/search?q='+search)


def mute():
    pyautogui.keyDown('fn')
    pyautogui.press('f5')


def news():
    newsapi = NewsApiClient(api_key='18e28850f4fb4b40b9c989ab3f6c94b6')
    speak("which topic")
    art = takeCommandMic()
    data = newsapi.get_top_headlines(q=art, language='en', page_size=5)
    newsdata = data['articles']
    for x, y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak(f'{x}{y["description"]}')
    speak("thats it for now i'll update you in some time")


def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)


def screenshorts():
    name_img = tt.time()
    name_img = 'E:\\projects\\project\\__pycache__\\screensh\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()


def trans():

    speak("please tell what to translate")
    sentence = takeCommandMic()

    speak("tell the language to translate")
    des = takeCommandMic()
    translator = Translator()
    trasalated_sent = translator.translate(sentence, src='en', dest=des)
    print(trasalated_sent.pronunciation)
    speak(trasalated_sent.pronunciation)


def takeCommandCMD():
    query = input("please tel me how can i help u?")
    return query


def main():
    wishme()
    while True:
        query = takeCommandMic().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'mail' in query:
            # email_list = {
            #     'test email': 'sagar.m0322@gmail.com'
            # }
            try:
                # speak('To Whom')
                # name = takeCommandMic()
                speak("what is the subject of the mail?")
                subject = takeCommandMic()
                speak('what should i say')
                content = takeCommandMic()
                receiver = "sagar.m0322@gmail.com"
                sendEmail(receiver, subject, content)
                speak('email sent')
            except Exception as e:
                print(e)
                speak('unable to send')
        elif 'news' in query:
            news()
        elif 'message' in query:
            user_name = {
                'Sindhu': '+91 9845525119'
            }
            try:
                speak('To Whom want to send whatsapp message')
                name = takeCommandMic()
                pho_no = user_name[name]
                speak("what is the subject of the mail?")
                message = takeCommandMic()
                sendwhatsapp(pho_no, message)
                speak('meassage has sent')
            except Exception as e:
                print(e)
                speak('unable to send')
        elif 'wikipedia' in query:
            speak("searching on wiki...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'youtube' in query:
            speak("what should i search in youtube")
            topic = takeCommandMic()
            pywhatkit.playonyt(topic)
        elif 'search' in query:
            searchongoogle()
        elif 'read' in query:
            text2speech()
        elif 'weather' in query:
            speak("which city")
            city = takeCommandMic()
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2ffed89c14ec6fa6f7fa8e3f475d84cd'
            res = requests.get(url)
            data = res.json()
            weather = data['weather'][0]['main']
            temp = data['main']['temp']
            desp = data['weather'][0]['description']
            temp = round((temp - 32) * 5/9)
            print(weather)
            print(temp)
            print(desp)
            speak(f'weather in {city} is')
            speak('Temperature :{} degree celcius'.format(temp))
            speak('weather is {}'.format(desp))
        elif 'open chrome' in query:
            speak('lunching chrome browser')
            codepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
            os.startfile(codepath)
        elif 'open document' in query:
            speak('opening the document')
            os.system('explorer C://{}'.format(query.replace('Open', '')))
        elif 'jokes' in query:
            speak(pyjokes.get_joke())
        elif 'screenshot' in query:
            screenshorts()
        elif 'brightness' in query:
            screenbright()
        elif 'remember' in query:
            speak("what should i remember?")
            data = takeCommandMic()
            speak("you said me to remember that"+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        elif 'mute' in query:
            mute()
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("you told me to remember that"+remember.read())
        elif 'translate' in query:
            trans()
        elif 'volume up' in query:
            pyautogui.press("volumeup")
        elif 'volume down' in query:
            pyautogui.press("volumedown")
        elif 'volume mute' in query:
            pyautogui.press('f5')
        # elif 'thank you' in query:
        #     thank()
        # elif 'Nothing' or 'no' in query:
        #     speak("have a greate day ")
        #     speak("bye")
        #     quit()
        elif 'offline' in query:
            speak("have a greate day ")
            speak("bye")
            quit()


if __name__ == "__main__":
    main()

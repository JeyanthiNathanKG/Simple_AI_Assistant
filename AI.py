import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import smtplib
import webbrowser
import os
import psutil
import pyautogui
import pyjokes
from textblob import TextBlob

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
voice_rate = 150
engine.setProperty('rate', voice_rate)
name = input(str("Enter Your name here: "))


def wish_you(audio):
    engine.say(audio)
    engine.runAndWait()


def intro_speak(audio):
    engine.say(audio)
    engine.runAndWait()


def play_music():
    song_dir = "D:\MyMusic"
    songs = os.listdir(song_dir)
    os.startfile(os.path.join(song_dir, songs[1]))


def time():
    intro_speak("The Time is ")
    time_at_now = datetime.datetime.now().strftime("%I %M %S")
    intro_speak(time_at_now)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    dat = int(datetime.datetime.now().day)
    intro_speak("Today date is...")
    intro_speak(dat)
    intro_speak(month)
    intro_speak(year)


def greetings():

    hour = datetime.datetime.now().hour

    if 6 <= hour <= 12:
        intro_speak("Good Morning"+name)
    elif 12 <= hour <= 18:
        intro_speak("Good afternoon"+name)
    elif 18 <= hour <= 23:
        intro_speak("Good evening "+name)
    else:
        intro_speak("Good night have a sweet dreams"+name)


def spell_check():
    query = instruction_to_assistant().lower()
    corrected_text = TextBlob(query)
    corrected_text.correct()
    for i in corrected_text:
        intro_speak(i)


def joke():
    intro_speak(pyjokes.get_joke())


def instruction_to_assistant():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
    except Exception as e:
        print(e)
        intro_speak("can you please say again")

        return "None"
    return query


def battery_and_cpu():
    usage = str(psutil.cpu_percent())
    intro_speak("CPU Is : " + usage)
    battery = str(psutil.sensors_battery())
    intro_speak("Battery percentage is : " + battery)


def open_mozilla():
    wish_you("what You want to search in browser..?")
    webbrowser.register('firefox',
                        None,
                        webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
    search = instruction_to_assistant().lower()
    webbrowser.get('firefox').open_new(search+".com")
    wish_you("Opening Mozilla firefox")


def screen_shoot():
    img = pyautogui.screenshot()
    img.save(r"D:\screenshot.png")
    intro_speak("Screenshot successfully")


def send_mail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 550)
    server.ehlo()
    server.starttls()
    server.login("sendermail@gmailcom", "password")
    server.sendmail("recievermail@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wish_you(" hello "+name)
    wish_you("Welcome back to AI Assistant")
    while True:

        query = instruction_to_assistant().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            wish_you("Thanks for using AI Assistant hope you'll enjoyed this")
            quit()
        elif "email" in query:
            try:
                print("redirect into mail page...")
                intro_speak("what should I say to them..?")
                content = instruction_to_assistant()
                to = "ReciverMail@gmail.com"
                send_mail(to, content)
                intro_speak("Mail has been send successfully")
                intro_speak(content)
                print(content)
            except Exception as e:
                print(e)
                intro_speak("unable to send mail..!!")
        elif "search in browser" in query:
            open_mozilla()
        elif "play songs" in query:
            play_music()
        elif "battery" in query:
            battery_and_cpu()
        elif "screenshot" in query:
            screen_shoot()
        elif "tell me a joke" in query:
            joke()
        elif "wishing" in query:
            greetings()
        elif "check my word" in query:
            intro_speak("Say which one you want find the spelling..?")
            spell_check()
        elif "wikipedia" in query:
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            intro_speak(result)
            print(str(result))
        elif "open file manager" in query:
            os.system('explorer D:')



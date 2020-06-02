import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install SpeechRecognition
import wikipedia as wk  # pip install wikipedia
import webbrowser as wb
import os
import pyjokes  # pip install pyjokes
import pyautogui  # pip install pyautogui
import psutil

# initializing the text-to-speech engine
engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak("Hi im jarvis")

# This function is for CPU and battery statistics


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU usage at "+usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

# Creating time and date functions to tell us time and date


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

# Function to take screenshot


def screenshot():
    img = pyautogui.screenshot()
    img.save("./ss.png")

# Function to crack Jokes


def jokes():
    joke = pyjokes.get_joke()
    speak(joke)


# On startup this function helps the JARVIS to Greet Us
def wishme():
    speak("Welcome back sir")

    hour = datetime.datetime.now().hour
    if 6 >= hour and hour < 12:
        speak("Good Morning sir")
    elif 12 >= hour and hour < 16:
        speak("Good Afternoon sir")
    elif 16 >= hour and hour < 24:
        speak("Good Evening sir")
    else:
        speak("Good Night sir")
    speak("Jarvis at your sevice,  how can i help you")

# Taking Voice Commands
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Sorry Sir but i am Unable to recognize your query, say it again please..")
        return "none"
    return query


# Main Function
if __name__ == "__main__":
    wishme()
    cpu()
    while True:
        query = takecommand().lower()

        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "offline" in query:
            speak("Ok sir going offline, take care, byee ")
            quit()

        elif "logout" in query:
            speak("System is Logging out")
            print("System is logging out")
            os.system("shutdown -1")

        elif "restart" in query:
            speak("System is Restarting")
            print("System is Resatarting")
            os.system("shutdown /r /t 1")

        elif "shutdown" in query:
            speak("System is shutting down")
            print("System is shutting down")
            os.system("shutdown /s /t 1")

        elif "play songs" in query:
            songs_dir = "E:\musicdir"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif "remember that" in query:
            speak("What should i remember ?")
            print("What should i remember ?")
            data = takecommand()
            speak("you said me to remember that " + data)
            print("you said me to remember that " + data)
            remember = open("remember.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("remember.txt", "r")
            speak("You said me to remember that "+remember.read())
            print("You said me to remember that "+remember.read())

        elif "screenshot" in query:
            speak("Taking screenshot...")
            print("Taking screenshot...")
            screenshot()
            speak("Done")
            print("Done")

        elif "chrome" in query:
            speak("what should i search ?")
            print("What should i search ?")
            search = takecommand().lower()
            wb.open_new_tab("https://www."+search+".com")

        elif "wikipedia" in query:
            speak('searching...')
            print("searching...")
            query = query.replace("wikipedia", "")
            result = wk.summary(query, sentences=2)
            print(result)
            speak(result)

        elif "jokes" or "joke" or "bored" in query:
            speak("Ok Im going to crack a joke")
            jokes()

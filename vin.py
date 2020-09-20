import speech_recognition
from datetime import date, datetime
import requests, json  # For weather
import pyttsx3

# Init
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
you = ""
robot_brain = ""

# robot's knowledge
now = datetime.now()
today = date.today()

# Function
def weather(city_name):
    api_key = "1520d85992106dbe0c323304bd31c0e8"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name.lower() + "&appid=" + api_key
    response = requests.get(complete_url)
    result = response.json()
    if result["cod"] != "404":
        weather = result["weather"][0]["main"]
        current_temperature = int(result["main"]["temp"] - 273)
        city = result["name"]
        robot_brain = "City: " + city + ", weather: " + weather + ", temperature: " + str(current_temperature) + " celsius"
    else:
        robot_brain = "name city invalid"
    return robot_brain

# Robot listening from mic
def listen_mic():
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        print("Robot: ...")
        audio = robot_ear.listen(mic)
    try: 
        you = robot_ear.recognize_google(audio, language='vi-VN')
        you =  you.lower()
        print("you: " + you)
        return you
    except: 
        you = ""
        print("you: " + you)
        return you

# AI
while True:
    you = listen_mic()
    if "hello" in you:
        robot_brain = "hello, how are you"
    elif "today" in you:
        robot_brain = today.strftime("%B-%d-%Y")
    elif "time" in you:
        robot_brain = now.strftime("%H hours %M minutes")
    elif "temperature" in you:
        robot_brain = "what's city"
        print("Robot_brain: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        you =  listen_mic()
        print("you: " + you)
        robot_brain = weather(you)
    elif "bye" in you:
        robot_brain = "see you"
        print("Robot_brain: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "what"
    print("Robot_brain: " + robot_brain)
    # Robot speak
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
  







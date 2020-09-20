import speech_recognition
from datetime import date, datetime
import requests, json  # For weather
from googletrans import Translator
from gtts import gTTS
import playsound

# Init
robot_ear = speech_recognition.Recognizer()
you = ""
robot_brain = ""

# robot's knowledge
now = datetime.now()
today = date.today()

# Function
def translate(word):
    translator = Translator()
    trans = (translator.translate(word, src='en', dest='vi')).text
    return trans

def say_vietnamese(text):
    tts= gTTS(text, lang='vi')
    file_name= 'speed.mp3'
    tts.save(file_name)
    playsound.playsound(file_name)


def weather(city_name):
    api_key = "1520d85992106dbe0c323304bd31c0e8"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    response = requests.get(complete_url)
    result = response.json()
    if result["cod"] != "404":
        weather = result["weather"][0]["main"]
        current_temperature = int(result["main"]["temp"] - 273)
        city = result["name"]
        robot_brain = "City: " + city + ", weather: " + weather + ", temperature: " + str(current_temperature) + " celsius"
    else:
        robot_brain = "Tên thành phố không đúng"
    return robot_brain

# Robot listening from mic
def listen_mic():
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        print("Robot: ...")
        audio = robot_ear.listen(mic)
    try: 
        you = robot_ear.recognize_google(audio, language='vi-VN')
    except: 
        you = "gdsGSD"
    print("you: " + you)

# AI
while True:
    listen_mic()
    if "Xin chào" in you:
        robot_brain = "Chào phi, bạn có khỏe không"
    elif "hôm nay" in you:
        robot_brain = today.strftime("%B-%d-%Y")
        # robot_brain = translate(robot_brain)
    elif "giờ" in you:
        robot_brain = now.strftime("%H hours %M minutes")
        # robot_brain = translate(robot_brain)
    elif "nhiệt độ" in you:
        robot_brain = "Thành phố gì ạ"
        print("Robot_brain: " + robot_brain)
        say_vietnamese(robot_brain)
        listen_mic()
        print("you: " + you)
        robot_brain =  translate(weather(you))
    elif "tạm biệt" in you:
        robot_brain = "Hẹn gặp lại"
        print("Robot_brain: " + robot_brain)
        say_vietnamese(robot_brain)
        break
    else:
        robot_brain = "Cảm ơn bạn"
    print("Robot_brain: " + robot_brain)
    # Robot speak
    say_vietnamese(robot_brain)
    # robot_mouth.runAndWait()







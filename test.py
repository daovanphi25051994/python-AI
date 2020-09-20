from gtts import gTTS
import playsound

text= 'Xin chào phi'

tts= gTTS(text, lang='vi')
file_name= 'speed.mp3'
tts.save(file_name)
playsound.playsound(file_name)
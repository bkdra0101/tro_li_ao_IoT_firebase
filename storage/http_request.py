

import requests as r

import serial
import time
from gtts import gTTS
import playsound
import os
import speech_recognition as sr

from tkinter import *
from PIL import Image , ImageTk

# ser = serial.Serial('COM6',9600)
#time.sleep(2)

def hear():
    print("listening : ....")
    r= sr.Recognizer()
#    source= sr.Microphone()
    with sr.Microphone()as source:  #mở Microphone mới và lưu với tên source,sau khi thoát with thì mic sẽ tắt
        print("Tôi: ",end='')
        audio = r.listen(source,phrase_time_limit= 3) #lưu lại câu nói của mình dưới dạng âm thanh là .mp3
        try:
            text= r.recognize_google(audio, language="vi-VN")
            print (text)
            #box1_(text)
            return str(text).lower()
        except:
            return None




def speak(text):
    #box2_(text)
    print("Dasha: "+ text)
    tts= gTTS(text = text, lang= "vi",slow= False) #chuyển text thành âm thanh qua API google
    tts.save("sound.mp3")                          #Sau khi gửi âm thanh về thì sẽ lưu lại dưới tên sound.mp3
    playsound.playsound("sound.mp3",True)          #phát file sound.mp3
    os.remove("sound.mp3") 

url= "http://192.168.1.107/"

s=r.get(url)

print(s.text)

speak ("bắt đầu wiffi")
while(True):
    you=hear()
    if you==None:
        speak("không nghe")
    elif "bật" in you:
        if "đèn1" in you :
            s=r.get("http://192.168.1.107/on1")
            print(s.text)
            speak("led on1 bật")

        if "đèn2" in you :
            s=r.get("http://192.168.1.107/on2")
            print(s.text)
            speak("led on2 bật")
    elif "tắt" in you:
        if "đèn1" in you :
            s=r.get("http://192.168.1.107/off1")
            print(s.text)
            speak("led on1 tắt")

        if "off2" in you :
            s=r.get("http://192.168.1.107/off2")
            print(s.text)
            speak("led off2 tắt")
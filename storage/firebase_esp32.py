import requests as r
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

url= "https://esp32-remote-51786-default-rtdb.firebaseio.com/.json"

json= {"on1":1,"on2":0}
#content= r.put(url=url,json=json)

#print(content.json()["on1"])

speak("chào cùng chơi nào")

while(True):
    you=hear()
    if you==None:
        speak("không nghe")


    elif "bật" in you:
        if "đèn 1" in you:
            json["on1"] =1
            content= r.put(url=url,json=json)
            speak("đèn 1 bật")
        if "đỏ 2" in you:
            json["on2"] =1
            content= r.put(url=url,json=json)
            speak("đèn 2 bật")

    elif "tắt" in you:
        if "đỏ 1" in you:
            json["on1"] =0
            content= r.put(url=url,json=json)
            speak("đèn 1 tắt")
        if "đỏ 2" in you:
            json["on2"] =0
            content= r.put(url=url,json=json)
            speak("đèn 2 tắt")
    elif "tạm biệt" in you:
        speak("bye bye")

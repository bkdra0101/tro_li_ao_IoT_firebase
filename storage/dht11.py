import serial
import time
from gtts import gTTS
import playsound
import os
import speech_recognition as sr

from tkinter import *
from PIL import Image , ImageTk

ser = serial.Serial('COM6',9600)
time.sleep(2)

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





speak("bắt đầu chạy")
while(True):
    you=hear()
    if you==None:
        speak("không nghe")
    if "nhiệt độ" in you:
        ser.write('t'.encode())
        s= str(ser.readline())
        s= s[2:]
        s=s.split("\\")[0]
        print (s)
        speak("nhiệt độ là" +s + "độ C")
    elif "độ ẩm" in you:
        ser.write('h'.encode())
        s= str(ser.readline())
        s= s[2:]
        s=s.split("\\")[0]
        print (s)
        speak("độ ẩm là" +s + "phần trăm")
    elif "bật" in you:
        if "đỏ 1" in you:
            ser.write('1'.encode())
            speak("đỏ 1 được bật")
        if "đỏ 2" in you:
            ser.write('3'.encode())
            speak("đỏ 2 được bật")

    elif "tắt" in you:
        if "đỏ 1" in you:
            ser.write('2'.encode())
            speak("đỏ 1 được tắt")
        if "đỏ 2" in you:
            ser.write('4'.encode())
            speak("đỏ 2 được tắt")
    elif "tạm biệt" in you:
        speak("bye bye")
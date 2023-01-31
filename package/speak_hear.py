
from gtts import gTTS
import playsound
import os
import speech_recognition as sr

from tkinter import *
from PIL import Image , ImageTk

#đồ họa
root = Tk()
root.title("Khang' ASSISTANT")
root.geometry("900x830")
root.iconbitmap("data_hinh\\background.jpg")

load= Image.open("data_hinh\\background.jpg")
render= ImageTk.PhotoImage(load)
img= Label(root,image=render)
img.place(x=0,y=0)

#tạo biến label để giúp hiển thị chữ ra màn hình
name= Label(root,text="Khang' ASSISTANT",fg="#45F848",bd=0,bg="#03152D")
name.config(font=("Transformers Movie",35))
name.pack(pady=10)

#box 1
#Tương tự tạo Label name 1 hiển thị chữ "Dasha hear" lên background
name1= Label(root,text="Dasha hear",fg="#F8E245",bd=0,bg="#03152D")
name1.config(font=("Transformers Movie",20))
name1.pack(pady=30)

#tạo một ô để hiển thị nội dung trợ lí ảo nghe được ra giao diện
box1=Text(root,width=48,height=8,font=("ROBOTO",16))
box1.pack(pady=0)

#box2
#tạo Label hiển thị text "ANNA speak"lên background
name2= Label(root,text="Dasha speak",fg="#F8E245",bd=0,bg="#03153D")
name2.config(font=("Transformers Movie",20))
name2.pack(pady=30)

#tạo một ô để hiển thị nội dung trợ lí ảo nghe được ra giao diện
box2=Text(root,width=48,height=8,font=("ROBOTO",16))
box2.pack(pady=0)

#tạo hàm để xuất Text ra box tương ứng đã tạo ở trên

def box1_(text):
    box1.delete(1.0,END)   #xóa nội dung cũ
    box1.insert(END, text) #viết nội dung mới vào 

def box2_(text):
    box2.delete(1.0,END)   #xóa nội dung cũ
    box2.insert(END, text) #viết nội dung mới vào 

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
            box1_(text)
            return str(text).lower()
        except:
            return None




def speak(text):
    box2_(text)
    print("Dasha: "+ text)
    tts= gTTS(text = text, lang= "vi",slow= False) #chuyển text thành âm thanh qua API google
    tts.save("sound.mp3")                          #Sau khi gửi âm thanh về thì sẽ lưu lại dưới tên sound.mp3
    playsound.playsound("sound.mp3",True)          #phát file sound.mp3
    os.remove("sound.mp3")                         #xóa file sound.mp3



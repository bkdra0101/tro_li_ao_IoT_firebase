

import speech_recognition as sr

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
            return str(text).lower()
        except:
            return None


from gtts import gTTS
import playsound
import os

def speak(text):
    print("Dasha: "+ text)
    tts= gTTS(text = text, lang= "vi",slow= False) #chuyển text thành âm thanh qua API google
    tts.save("sound.mp3")                          #Sau khi gửi âm thanh về thì sẽ lưu lại dưới tên sound.mp3
    playsound.playsound("sound.mp3",True)          #phát file sound.mp3
    os.remove("sound.mp3")                         #xóa file sound.mp3



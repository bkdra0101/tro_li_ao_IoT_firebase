
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



from hear import *
from storage.trash.speak import *
from datetime import date, datetime, time
import webbrowser
import time
import os
#from test import *

def shoping():
    speak.speak("bạn muốn mua ở đâu : Tiki , Shopee, biên hòa gear, memoryzone")
    you= hear.hear()
    if "Tiki" in you:
        webbrowser.open("https://tiki.vn/")
        time.sleep(2)
        speak("Tiki đã mở")        
    elif "Shopee" in you:
        webbrowser.open("https://shopee.vn/")
        time.sleep(2)
        speak("Shopee đã mở") 
    if "biên hòa gear" in you:
        webbrowser.open("https://bienhoagear.com/")
        time.sleep(2)
        speak("biên hòa gear đã mở")  
    if " memoryzone" in you:
        webbrowser.open("https://memoryzone.com.vn/")
        time.sleep(2)
        speak("memoryzone đã mở")   

speak("xin chào mọi người mình là Dasha")

while (True):
    you = hear()
    if you == None:
        speak("Em chưa nghe được bạn nói, nói lại đi")
    elif "hôm nay" in you or "bây giờ"in you:
        now= datetime.now()
        if "giờ"in you:
            t= now.strftime("%H giờ , %M phut , %S giây")
            speak(t)
        if "ngày"in you:
            t=now.strftime("ngày %d, tháng %m , năm %Y")
            speak(t)
    elif "mở" in you and "hình" in you:
        os.startfile("D:\hinh\dasha taran (@taaarannn) • Instagram photos and videos_files\1173119_824656297660701_110518732_a.jpg")
    elif "mở" in you:
        if "facebook" in you:
            webbrowser.open("https://www.facebook.com/")
            time.sleep(2)
            speak("Facebook đã mở")
        if "zalo"in you:
            webbrowser.open("https://chat.zalo.me/")
            time.sleep(2)
            speak("zalo đã mở")
        if "youtube"in you:
            webbrowser.open("https://www.youtube.com/")
            time.sleep(2)
            speak("youtube đã mở")
        if "trang online"in you:
            webbrowser.open("https://online.hcmute.edu.vn/")
            time.sleep(2)
            speak("trang online đã mở") 
    elif "mua sắm" in you: 
        shoping()         
    elif "tạm biệt" in you:
        speak(" Hẹn gặp lại ")
        break
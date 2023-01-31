from package._init_ import*
from package.library import*
from package.function import*
from package.speak_hear import*
from threading import Thread
from datetime import timedelta,time,datetime, date , time


def tro_ly_ao():
    f= open("database\\answer.txt",mode="r",encoding="utf8")
    answer=f.read().split("\n")

    speak("xin chào mọi người, mình là Dasha")
    while True:
        you= hear()

        if you == None:
            speak("tôi không nghe được")
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
           # shoping()  
            webbrowser.open("https://online.hcmute.edu.vn/")       
        elif "tạm biệt" in you:
            speak(" Hẹn gặp lại ")
            break        
        else:
            index= handle_data(you)
            speak(answer[index])

Thread1= Thread(target= tro_ly_ao)
Thread1.start()

root.mainloop()



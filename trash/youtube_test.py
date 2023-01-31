

import webbrowser
from youtube_search import YoutubeSearch
import time

def search_youtube(text):
    #sử dụng vòng while tìm kiếm đén khi nào có kết quả trả về
    while True:
        #biến results lưu lại kết quả trả về dưới dạng dữ liệu Dictionary
        result= YoutubeSearch(text,max_results=10).to_dict()
        if result:
            break
    url= "https://www.youtube.com"+result [0]["url_suffix"]
    webbrowser.open(url)
    time.sleep(2)
    print(" Youtube đã được tìm kiếm")

search_youtube("họ yêu ai mất rồi")
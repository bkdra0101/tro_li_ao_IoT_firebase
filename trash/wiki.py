import wikipedia
wikipedia.set_lang("vi")

def search_wiki(text):
    try:
        #Do chuỗi infor gửi về khá dài nên chúng ta chia thành các đoạn và lưu ở  dạng list
        infor= wikipedia.summary(text).split("\n")
        print(infor[0] )#.split(".")[0])
        for a in infor [1:]:
            print ("bạn muốn nghe thêm không ?")
            ans=input()
            if "có" not in ans:
                break
            print(a)
        print("cảm ơn bạn đã nghe.")
    except:
        print("không tìm thấy tài liệu")

search_wiki("yua mikami")
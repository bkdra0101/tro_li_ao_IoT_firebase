import numpy
#mở file question .txt và đọc file lưu các câu hỏi ở dạng list
f= open("database\\question.txt",mode="r",encoding="utf8")
ques=f.read().split("\n")
# tạo hàm xử lí dữ liệu
def handle_data(text):
    #chia câu hỏi thành các từ riêng biệt
    text= text.split("")
    #khỏi tạo list rỗng để lưu tỉ lệ % giống nhau giữa câu hỏi người dùng và data question mình tạo
    ans=[]

    #tính toán tỷ lệ phần trăm từng câu hỏi trong database bằng for
    for s in ques:
        #khởi tạo biến đếm số từ trùng lặp trong câu hỏi người dùng và câu hỏi database
        count=0
        #tính toán số từ trùng lặp
        for i in text:
            if i in s:
                #cứ mỗi lần có từ trùng lặp thì count cộng thêm 1
                count +=1
        #sau khi tính được số từ trùng lặp thì sẽ chia cho độ dài của câu hỏi trong database để lấy tỷ lện % trùng lặp
        ratio= count *100 /len(s)
        #append()tỷ lệ % đó vào list
        ans.append(ratio)
    #trả về thứ tự câu hỏi có tỷ lệ % tương ứng cao nhất
    print(ans)
    return numpy.argmax(ans)

#đọc file answer.txt và lưu các câu hỏi ở dạng list
'''f= open("database\\answer.txt",mode="r",encoding="utf8")
answer=f.read().split("\n")'''

"""index= handle_data("bây giờ bạn bao nhiêu tuổi")
print(answer[index])"""


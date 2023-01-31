from threading import Thread
import time

# <ten>= Thread(target=<funtion>)

#<te>.start(
def printname(text):
    print(text)

def printadd(text):
    print(text)

Thread1=Thread(target= printname("khang"))
Thread1.start()

Thread2=Thread(target= printadd("đẹp trai"))
Thread2.start()
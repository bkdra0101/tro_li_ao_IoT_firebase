
import serial
import time
ser = serial.Serial('COM6',9600)


def SerialWrite(s):
    ser.write(s.encode())

while True:
    s= str(input())
    if "bật led" in s:
        SerialWrite(s)
    elif "bật led" in s:
        SerialWrite(s)
    elif "bật led" in s:
        SerialWrite(s)
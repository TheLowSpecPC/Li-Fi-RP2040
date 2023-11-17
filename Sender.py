from machine import Pin
from time import sleep
import math

las = Pin(17, Pin.OUT)
las.off()

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

while True:
    a=0
    lis = toBinary(input())
    print(lis)

    las.on()
    sleep(0.6)
    las.off()
    sleep(1.5)
    for i in lis:
        for j in str(i):
            if j == '1':
                las.on()
                sleep(0.5)
            elif j == '0':
                las.off()
                sleep(0.5)
        a+=1
        if a == len(lis):
            las.off()
            print('Done')
        else:
            print('next')
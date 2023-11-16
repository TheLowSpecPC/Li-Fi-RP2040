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

lis = toBinary(input())
print(lis)

for i in lis:
    for j in str(i):
        if j == '1':
            las.off()
            sleep(0.5)
            las.on()
            sleep(0.5)
            las.off()
        elif j == '0':
            las.off()
            sleep(0.2)
            las.on()
            sleep(0.2)
            las.off()
            sleep(0.2)
            las.on()
            sleep(0.2)
            las.off()
    print('next')
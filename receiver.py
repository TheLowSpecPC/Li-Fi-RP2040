from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
from time import sleep
import math

I2C_ADDR     = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

sda = Pin(16, Pin.PULL_UP)

scl = Pin(17, Pin.PULL_UP)

i2c = I2C(0, sda=sda, scl=scl, freq=400000)
print(i2c.scan())
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

diode = machine.ADC(Pin(27))
but = Pin(15, Pin.IN, Pin.PULL_DOWN)
 
def toString(a):
  l=[]
  m=""
  for i in a:
    b=0
    c=0
    k=int(math.log10(i))+1
    for j in range(k):
      b=((i%10)*(2**j))   
      i=i//10
      c=c+b
    l.append(c)
  for x in l:
    m=m+chr(x)
  return m

while True:
    if diode.read_u16() >= 20000:
        lcd.move_to(0,0)
        lcd.putstr("Initialized")
        print('Initialized')
        sleep(3)
        lcd.clear()
        while True:
            a=0
            byt=""
            while a<7:
                if diode.read_u16() >= 20000:
                    byt=byt+"1"
                else:
                    byt=byt+"0"
                sleep(0.5)
                a+=1
            print(byt)
            if byt != "0000000":
                out = toString([int(byt)])
                lcd.putstr(out)
                print(out)
            if but.value() == 1:
                break
        
    sleep(0.5)
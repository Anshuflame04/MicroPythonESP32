from machine import Pin
import time

LED = Pin(2, Pin.OUT)  #Pin 2 as Output(LED)
BUT = Pin(0, Pin.IN)    #Pin 0 as Input btn

while True:
    but_status = BUT.value()
    if(but_status==False):
        LED.value(1)
    else:
        LED.value(0)


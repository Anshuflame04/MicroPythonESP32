## **Starting with MicroPython for ESP32**
* **Step-1:** Install Thonny IDE 
* **Step-2:** Then configure interpreter for MicroPython(ESP32)

Now setup is done

## Basic imports
* **machine library:** Provides access to hardware specific functions such as controlling GPIO pins
* **time library:** Provides functions related to time.Ex-> sleep(1)

## **Project 1(Blinking LED)**

```py
import machine  
import time

LED = machine.Pin(2, machine.Pin.OUT)    #Initializing Pin 2 as Output pin for controlling LED

while True:      #For infinite blinking at a time difference of 1 second
    LED.value(1)
    time.sleep(1)
    LED.value(0)
    time.sleep(1)
```

## **Project 2(Button Interaction with LED)**
```py
from machine import Pin
import time

LED = Pin(2, Pin.OUT)
BUT = Pin(0, Pin.IN)  #configuring Pin 0 as Input pin, where button is connected

while True:
    but_status = BUT.value()      
    if(but_status==False):      #when button is pressed, led will turn ON
        LED.value(1)
    else:
        LED.value(0)
```



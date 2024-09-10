## Basic imports
* **machine library:** Provides access to hardware specific functions such as controlling GPIO pins
* **time library:** Provides functions related to time.Ex-> sleep(1)
* **dht library:** Provides functions for interacting with DHT sensors


## **Project 3(Temperature and Humidity Using DHT sensor)**

```py
from machine import Pin
import dht
import time


sensor_data = dht.DHT11(Pin(14))   

def call_dht():
    sensor_data.measure()    #tells the sensor to read temp and humidity
    temp = sensor_data.temperature()
    hum = sensor_data.humidity()
    print("Temp:", temp, "Humidity:", hum)
    
while True:
    call_dht()
    time.sleep(1)

```

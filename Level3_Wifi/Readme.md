## **Network module in ESP32**


## Basic imports
* **machine library:** Provides access to hardware specific functions such as controlling GPIO pins
* **network module:** Provides functions for configuring network interfaces 

## **Project 4(Getting nearby wifi networks)**
To display all the available nearby wifi networks by (**scan method**) 
* * **network.STA_IF:** creates a WLAN object in station mode, used for connecting as Client.
```py
import network

wifi = network.WLAN(network.STA_IF)    #Creates WLAN object in station mode
wifi.active(True)

networks = wifi.scan()

print(networks)

```
**Output**
```txt
[(b'', b'`"2\xfa\xe3"', 6, -60, 1, False), (b'TRIDENTHOSTEL', b'b"2\x9a\xe3"', 6, -61, 3, False), (b'', b'`"2\xfa\xb7\x8a', 1, -68, 1, False), (b'TRIDENTHOSTEL', b'b"2\x9a\xb7\x8a', 1, -68, 3, False), (b'JioPrivateNet', b'\x88\xb1\xe1s\x06\xa0', 6, -74, 5, False), (b'', b'`"2\xfb\x1bv', 1, -75, 1, False), (b'TRIDENTHOSTEL', b'b"2\x9b\x1bv', 1, -76, 3, False), (b'TRIDENTHOSTEL', b'b"2\x94\x06*', 11, -84, 3, False), (b'JioPrivateNet', b"\x88\xb1\xe1s'\x00", 11, -84, 5, False), (b'TRIDENTHOSTEL', b'b"2\x9b\n\xd6', 11, -85, 3, False), (b'', b'`"2\xfb\n\xd6', 11, -86, 1, False), (b'JioPrivateNet', b'\x88\xb1\xe1s\t\x00', 11, -89, 5, False), (b'TRIDENTHOSTEL', b'b"2\x9a\xb6\xfa', 11, -94, 3, False)]
```

## **Project 5(Setting Hotspot in ESP32)**
* * **network.STA_IF:** Creates WLAN object in Access Point mode
* * **wifi.ifconfig:** returns IP configuration of ESP
```py

import network

wifi = network.WLAN(network.AP_IF)
wifi.active(True)

wifi.config(essid = "AnshuESP", password = '12345678', authmode=network.AUTH_WPA_WPA2_PSK )

#For open network
#wifi.config(essid = "AnshuWIFI" )


print(wifi.ifconfig())
```
**Output**
```txt
('192.168.4.1', '255.255.255.0', '192.168.4.1', '0.0.0.0')
```

## **Project 6(Connecting to WIFI using ESP32)**
Trying to connect to wifi, if wifi not connected -> then it will come out of the loop after 5 sec
```py
import network
import time

timeout = 0

wifi = network.WLAN(network.STA_IF)

#Restarting wifi
wifi.active(False)
time.sleep(0.5)
wifi.active(True)

wifi.connect('wifianshu','*********')

if not wifi.isconnected():
    print("Connecting..")
    while (not wifi.isconnected() and timeout < 5):
        print(5 - timeout)
        timeout = timeout + 1
        time.sleep(1)


if wifi.isconnected():
    print("Connected")
else:
    print("Time OuT")
```
**Output(if not connected)**
```txt
Connecting..
5
4
3
2
1
Time OuT
```

## **Wifi and Hotspot Modes using External switch using ESP32**


## Basic imports
* **machine library:** Provides access to hardware specific functions such as controlling GPIO pins
* **network module:** Provides functions for configuring network interfaces 
* **_thread module:** for running tasks concurrently

## **Task**
* To  connect to wifi if SSID and password are stored 
* If not, then turn on the Access Point Mode(Hotspot)
* connecting to the wifi of ESP, when user will give the SSID and password of a network, its details will be stores in ESP memory
* And it will connect to that wifi network
* On pressing the external switch for 5 seconds, it will forget the SSID and passwords, and it will turn back to Access Point mode.
* Light will blink in Hotspot mode
* And light will glow constanlty if connected to wifi

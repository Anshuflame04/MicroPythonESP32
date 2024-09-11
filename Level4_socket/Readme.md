## **Server to control  LED on an web page**


## Basic imports
* **machine library:** Provides access to hardware specific functions such as controlling GPIO pins
* **network module:** Provides functions for configuring network interfaces
* **time:** Provides functions related to time
* **usocket:** Provides low-level network communiocation functionalities

## **Project 9**
* First, connecting to a wifi network 
* Then creating a web page for LED interaction
* Initializing a socket wiht IPv4 and TCP protocol
* Then hosting the website using **.bind** function
* storing the connection address of the new client connected using **.accept** function
* Then On the request of user, LED works(OFF or ON)

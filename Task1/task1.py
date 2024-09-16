import network
import socket
import time
import machine
import _thread  # For running concurrent tasks

# GPIO configuration
led = machine.Pin(2 , machine.Pin.OUT)
button = machine.Pin(33, machine.Pin.IN, machine.Pin.PULL_UP) 

# Wi-Fi credentials storage
def read_credentials():
    try:
        with open('wifi_credentials.txt', 'r') as f:
            ssid = f.readline().strip()
            password = f.readline().strip()
            return ssid, password
    except OSError:
        return None, None

def write_credentials(ssid, password):
    with open('wifi_credentials.txt', 'w') as f:
        f.write(ssid + '\n')
        f.write(password + '\n')

def clear_credentials():
    with open('wifi_credentials.txt', 'w') as f:
        f.write('')  # Clears the file

# Test Wi-Fi connection
def test_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    ssid, password = read_credentials()
    if ssid and password:
        print("Connecting to Wi-Fi...")
        wlan.connect(ssid, password)

        for _ in range(20):
            if wlan.isconnected():
                print("Connected to", ssid)
                return True
            time.sleep(0.5)

        print("Failed to connect to Wi-Fi.")
    return False

#For constant glow
def const_led():
    while True:
        led.on()

# For  blinking LED
def blink_led():
    while True:
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)

# Launch AP and start web server for setting Wi-Fi credentials
def start_ap():
    wlan = network.WLAN(network.AP_IF)
    wlan.active(True)
    wlan.config(essid='AnshuESP')
    print("Access Point created. Connect to 'AnshuESP' and set credentials.")

    # Start the LED blinking in AP mode
    _thread.start_new_thread(blink_led, ())  # Start blinking in a separate thread

    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Listening on', addr)

    while True:
        cl, addr = s.accept()
        print('Client connected from', addr)
        request = cl.recv(1024)
        request = str(request)

        if '/setting?' in request:
            params = request.split('/setting?')[1].split(' ')[0]
            ssid = params.split('&')[0].split('=')[1]
            password = params.split('&')[1].split('=')[1]
            
            ssid = ssid.replace('%20', ' ')
            password = password.replace('%20', ' ')
            write_credentials(ssid, password)

            response = """\
HTTP/1.1 200 OK

Wi-Fi credentials saved! Please reboot the ESP.
"""
            cl.send(response)
            cl.close()
            
            # Attempt to reconnect to Wi-Fi after saving credentials
            if test_wifi():
                print("Successfully connected to Wi-Fi.")
                const_led() # LED stays on in Wi-Fi mode
            else:
                print("Failed to connect. Starting Access Point...")
                start_ap()  # Enter AP mode with LED blinking

        response = """\
HTTP/1.1 200 OK

<!DOCTYPE html>
<html>
    <body>
        <h1>Enter Wi-Fi Credentials</h1>
        <form action="/setting" method="get">
            SSID: <input name="ssid"><br>
            Password: <input name="password"><br>
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
"""
        cl.send(response)
        cl.close()

# Monitor button press for 5 seconds to clear credentials and switch to AP mode
def monitor_button_press():
    press_time = 0
    while True:
        if not button.value():  # Button pressed
            press_time += 1
            time.sleep(1)

            if press_time >= 5:  # Button held for 5 seconds
                print("Button held for 5 seconds. -----> Clearing credentials and entering AP mode.")
                clear_credentials()
                start_ap()  # Enter AP mode
        else:
            press_time = 0  # Reset press time if button released
        time.sleep(0.1)

# Main setup
def setup():
    print("Starting...")
    
    # Check if already connected to Wi-Fi
    if test_wifi():
        print("Successfully connected to Wi-Fi.")
        led.on()  # LED in Wi-Fi mode
    else:
        print("Failed to connect. Starting Access Point...")
        start_ap()  # Enter AP mode with LED blinking

setup()
monitor_button_press()



import network

wifi = network.WLAN(network.AP_IF)
wifi.active(True)

wifi.config(essid = "AnshuESP", password = '12345678', authmode=network.AUTH_WPA_WPA2_PSK )

#For open network
#wifi.config(essid = "AnshuWIFI" )


print(wifi.ifconfig())


# load libraries
import network
import utime as time

from client import Server

def connect_wifi():

    # Client
    wlan = network.WLAN(network.STA_IF)

    # define variables
    wifi_names = ['ssid1', 'ssid2', 'ssid3']
    wifi_passwords = ['password1', 'password2', 'password3']

    #wifi_names = ['wifiname1', 'wifiname2', 'wifiname3']
    #wifi_passwords = ['wifipassword1', 'wifipassword2', 'wifipassword3']

    # activate WiFi interface
    wlan.active(True)
    correct_wifi = 0

    # scan for wifi connections
    wifi_found = False
    wifi_list = []
    for i in wlan.scan():
        wifi_list.append(i[0].decode('utf-8'))
    print(wifi_list)
    for i in wifi_names:
        if i in wifi_list:
            correct_wifi = wifi_names.index(i)
            wifi_found = True
            break

    if wifi_found:
        print('wifi found')
    else:
        print('No accessable wifi found')

    #connect to choosen wifi network
    wlan.connect(wifi_names[correct_wifi], wifi_passwords[correct_wifi])

    # check connection status
    print('Waiting for WiFi connection...')

    while not wlan.isconnected() and wlan.status() >= 0:
        time.sleep(1)

    if wlan.status() != 3:
        print('Error connecting to ', wifi_names[correct_wifi])

    if wlan.isconnected():
        print('Wifi connected\nStatus ', wlan.status())
        print(wlan.ifconfig())
        status = wlan.ifconfig()
        pico_ip = status[0]
        print('IP: ' + pico_ip)

        print('\n')
        serv = Server(True)
    else:
        print('WiFi not connected\nStatus: ', wlan.status())

        print('\n')
        serv = Server(False)

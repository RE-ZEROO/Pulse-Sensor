import  machine
from machine import Pin
import time
from time import sleep
import network
import socket
from main import adc_reader


class Server:
    def __init__(self, wifi = False):
        if(wifi == True):
            s = self.setup_wifi_server_network()
            print('Wifi Server')
        else: 
            s = self.setup_local_server_network()
            print('Local Server')
        
        while True:
            client, client_addr = s.accept()
            request = client.recv(1024)
            request = str(request)
            #request = request.decode("utf-8")
            #print('request:', request)
            request_url = request.split()[1]
            print('request_url:', request_url)

            css = request_url.find('.css')
            js = request_url.find('.js')

            if(css > 0):
                print('css reqeusted')
                response = self.get_request_file('./style.css')
                client.send('HTTP/1.0 200 OK\r\nContent-type: text/css\r\n\r\n')
            elif(js > 0):
                print('js reqeusted')
                response = self.get_request_file('./main.js')
                client.send('HTTP/1.0 200 OK\r\nContent-type: text/javascript\r\n\r\n')
                sleep(2)
            #else:
             #   response = self.get_html('./index.html', adc_reader())
              #  client.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
            else:
                response = self.get_request_file('./index.html')
                client.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')



            if(request_url.find('/data') > -1):
                print('data requested')
                response = str(adc_reader())
                #response = self.get_html('./index.html', adc_reader())
            #else:
                #response = self.get_html('./index.html', adc_reader())
                #client.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')


            #client.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
            client.send(response)
            client.close()
        
        
    def get_html(self, html_name, data):
        with open(html_name, 'r') as file:
            html = file.read()
            content = html.replace("<h3 id=\"pulseData\">70</h3>", "<h3 id=\"pulseData\">{}</h3>".format(data))

        sleep(0.5)

        return content
    
    def get_request_file(self, html_name):
        with open(html_name, 'r') as file:
            file_requested = file.read()
        
        return file_requested


    def setup_wifi_server_network(self):
        #Get ip address
        status = network.WLAN(network.STA_IF).ifconfig()
        pico_ip = status[0]

        #Open socket
        addr = (pico_ip, 80)
        s = socket.socket()
        s.bind(addr)
        s.listen(1)
        print('listening on ', addr)

        return s

    def setup_local_server_network(self):
        ssid = 'Pico Access Point'
        password = 'password'

        print('\n')
        print('Starting access point...')

        ap = network.WLAN(network.AP_IF)
        ap.config(essid=ssid, password=password)
        ap.active(True)

        wait_counter = 0
        while ap.active()== False:
            print("Waiting " + str(wait_counter))
            time.sleep(0.5)
            pass
        
        print('Access point active')
        print('IP: ', ap.ifconfig()[0])

        addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
        s = socket.socket()
        s.bind(addr)
        s.listen(1)
        print('Listening on ', addr)

        return s
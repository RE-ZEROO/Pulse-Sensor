import  machine
from machine import Pin
from time import sleep
import machine

import networking

sda=machine.Pin(20)
scl=machine.Pin(21)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)

led = Pin("LED", Pin.OUT)
led.off()
analog_value = machine.ADC(27)


def main():
    #networking.connect_wifi()

    while(True):
        adc_reader()


    #Scan for I2C devices
    '''print('Scan i2c bus...')
    devices = i2c.scan()
    
    if len(devices) == 0:
        print("No i2c device !")
    else:
        print('i2c devices found:',len(devices))
    
    for device in devices:  
        print("Decimal address: ",device," | Hexa address: ",hex(device))'''

    

def adc_reader():
    '''while True:
        reading = analog_value.read_u16()

        print("ADC: ", reading)
        sleep(1) #To low and it crashes on refresh. Default = 3

        if(reading < 4500):
            print("Something is blocking the sensor")
            led.on()
        else:
            led.off()

        print("=-=-=-=-=-=")

        return reading'''
    
    reading = analog_value.read_u16()

    print("ADC: ", reading)
    sleep(1) #To low and it crashes on refresh. Default = 3

    if(reading < 4500):
        print("Something is blocking the sensor")
        led.on()
    else:
        led.off()

    print("=-=-=-=-=-=")

    return reading



if __name__ == '__main__':
    main()
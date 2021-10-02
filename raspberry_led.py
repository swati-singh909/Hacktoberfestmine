'''
from RPi import GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pin=14
GPIO.setup(led_pin,GPIO.OUT)
print("Enter 1/0 to turn led on/off or any other number to exit from the program ")
led_status=0
while(led_status==0 or led_status==1):
    led_status=int(input())
    if led_status==0 or led_status==1:
        GPIO.output(led_pin,led_status)
    else:
        print("Exiting------------")
        break

'''

from RPi import GPIO
import requests
import json
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pin=14
GPIO.setup(led_pin,GPIO.OUT)

read_url="https://api.thingspeak.com/channels/1378XXX/feeds.json?api_key=6Q60UV0ORI39XXXX&results=1"
r=requests.get(read_url)
raw_data=r.json()["feeds"][-1]["field1"]

#print("Enter 1/0 to turn led on/off or any other number to exit from the program ")
#led_status=0
while(raw_data==0 or raw_data==1):
    #led_status=int(input())
    if raw_data==0 or raw_data==1:
        GPIO.output(led_pin,raw_data)
    else:
        print("Please enter 0 or 1 for off and on")
        break

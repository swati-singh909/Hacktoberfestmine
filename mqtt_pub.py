import paho.mqtt.client as client
from time import sleep
cl=client.Client("client1")
print("connecting")
#broker="broker.emqx.io"
cl.connect("localhost")
print("connected")
while(1):
    msg=input("Enter data : ")
    cl.publish("tests",msg)
    print("published")

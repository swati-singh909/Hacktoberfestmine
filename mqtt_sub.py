import paho.mqtt.client as client
from time import sleep

def on_message(cl,userdata,msg):
    print(msg.topic+" : "+str(msg.payload.decode("utf-8")))

cl=client.Client("client2")

while(1):
    cl.connect("broker.emqx.io")
    cl.loop_start()
    cl.subscribe("tests")
    cl.on_message=on_message
    sleep(1)
    cl.loop_stop()

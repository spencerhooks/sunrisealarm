#!/usr/bin/python
import time, sys, schedule
import paho.mqtt.client as mqtt
from pyplaybulb import playbulb

bulb = playbulb('CD:B3:4B:0A:AC:E6')

onoff_state = "initial"
connected = False

# function to detect connection to the mqtt broker and subscribe to the correct topics
def on_connect(client, userdata, msg, rc):
    client.subscribe([("home/bedroom/sunrise/set", 0), ("home/bedroom/sunrise/scheduler", 0)])

# function called when message received on home/bedroom/sunrise/set topic
def switch_message(client, userdata, msg):
    global onoff_state
    onoff_state = msg.payload
    client.publish("home/bedroom/sunrise", payload=msg.payload, retain=True) # publish to state topic to confirm the message was received
    if (msg.payload == "ON"): # flash the light green to acknowledge the ON message was recieved
        bulb.flash(duration=3, interval=1, wrgb_color='0000FF00')
        print "Sunrise ON"
        sys.stdout.flush() # flush the output buffer so the output is immediately sent (useful when redirecting)
    elif (msg.payload == "OFF"): # flash the light red to acknowldge the OFF message was received
        bulb.flash(duration=3, interval=1, wrgb_color='00FF0000')
        print "Sunrise OFF"
        sys.stdout.flush() # flush the output buffer so the output is immediately sent (useful when redirecting)

def schedule_message(client, userdata, msg):
    if (onoff_state == "ON" and msg.payload == "GO"):
        bulb.sunrise(sunrise_length=1800)
        client.publish("home/bedroom/sunrise/scheduler", payload="STOP", retain=True) # publish to scheuler topic to turn off again


client = mqtt.Client()
client.on_connect = on_connect

client.message_callback_add("home/bedroom/sunrise/set", switch_message)
client.message_callback_add("home/bedroom/sunrise/scheduler", schedule_message)

# connect to the MQTT broker and handle exceptions in case this is called before the network is setup
while (connected == False):
    try:
        client.connect("bunker", 1883, 60)
        client.loop_start()
        connected = True
    except:
        time.sleep(1)

# if run with argument -now then trigger sunrise immediately, then start schedule
try:   
    if (sys.argv[1] == "-now"):
        time.sleep(10)
        bulb.sunrise(sunrise_length=10)
except: pass

while True:
    time.sleep(1)
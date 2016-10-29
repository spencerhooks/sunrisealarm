#!/usr/bin/python

import time, sys
import paho.mqtt.client as mqtt
from pyplaybulb import playbulb

bulb = playbulb('CD:B3:4B:0A:AC:E6')

onoff_state = "initial"
connected = False
sunrise_mid = "initial" # global variable for tracking message ID

# function to detect connection to the mqtt broker and subscribe to the correct topics
def on_connect(client, userdata, msg, rc):
    client.subscribe([("home/bedroom/sunrise/set", 0), ("home/bedroom/sunrise/scheduler", 0)])

# function called when message received on home/bedroom/sunrise/set topic
def switch_message(client, userdata, msg):
    global onoff_state
    global sunrise_mid # set global message ID so we can check which one was published later
    onoff_state = msg.payload
    (result, sunrise_mid) = client.publish("home/bedroom/sunrise", payload=msg.payload, retain=True, qos=1) # publish to state topic to confirm the message was received

def schedule_message(client, userdata, msg):
    if (msg.payload == "GO"): # only run when the message was GO
        client.publish("home/bedroom/sunrise/scheduler", payload="STOP", retain=True, qos=1) # publish to scheduler topic to turn off again
        if (onoff_state == "ON"): # if alarm is on run the sunrise
            bulb.sunrise(sunrise_length=1800)

def on_publish(client, userdata, mid):
    if (mid == sunrise_mid): # if the message published was confirmation sent to home/bedroom/sunrise
        if (onoff_state == "ON"): # flash the light green to acknowledge the ON message was recieved
            bulb.flash(num_flashes=3, flash_length=1, wrgb_color='0000FF00')
            print "Sunrise ON"
            sys.stdout.flush() # flush the output buffer so the output is immediately sent (useful when redirecting)
        elif (onoff_state == "OFF"): # flash the light red to acknowldge the OFF message was received
            bulb.flash(num_flashes=3, flash_length=1, wrgb_color='00FF0000')
            print "Sunrise OFF"
            sys.stdout.flush() # flush the output buffer so the output is immediately sent (useful when redirecting)


client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

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

# if run with argument -now then trigger sunrise immediately
try:   
    if (sys.argv[1] == "-now"):
        time.sleep(10)
        bulb.sunrise(sunrise_length=10)
except: pass

while True:
    time.sleep(1)
#!/usr/bin/python
import time, sys, schedule
import paho.mqtt.client as mqtt
from pyplaybulb import playbulb

bulb = playbulb('CD:B3:4B:0A:AC:E6')

payload = "initial"
connected = False

# function to detect connection to the mqtt broker and subscribe to the correct topic
def on_connect(client, userdata, msg, rc):
    client.subscribe("home/bedroom/sunrise/set")

# function called when message received on subscribed topic
def on_message(client, userdata, msg):
    global payload
    payload = str(msg.payload)
    client.publish("home/bedroom/sunrise", payload=payload, retain=True) # publish to state topic to confirm the message was received

# function called when a message is published, used here to confirm the state change message was received by flashing the light
def on_publish(client, userdata, msg):
    if (payload == "ON"): # flash the light green to acknowledge the ON message was recieved
        bulb.flash(duration=3, interval=1, wrgb_color='0000FF00')
        print "Sunrise ON"
        sys.stdout.flush() # flush the output buffer so the output is immediately sent (useful when redirecting)
    elif (payload == "OFF"): # flash the light red to acknowldge the OFF message was received
        bulb.flash(duration=3, interval=1, wrgb_color='00FF0000')
        print "Sunrise OFF"
        sys.stdout.flush() # flush the output buffer so the output is immediately sent (useful when redirecting)

def job():
    bulb.sunrise(sunrise_length=1800)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

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

schedule.every().day.at("05:30").do(job)

while True:
    if (payload == "ON"):
        schedule.run_pending()
    time.sleep(1)
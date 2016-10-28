#!/usr/bin/python

#Simple script that is called by Cron at the scheduled time. Script sends mqtt message that tells the sunrise script to begin the sunrise now.

import time
import paho.mqtt.client as mqtt


# function that is called on initial connection to mqtt broker
def on_connect(client, userdata, msg, rc):
    client.publish("home/bedroom/sunrise/scheduler", payload="GO") # send message on scheduler topic so surise starts now
    print "publish GO message"

client = mqtt.Client()
client.on_connect = on_connect

client.connect("bunker", 1883, 60)
client.loop_start()
time.sleep(10)
print "executing scheduler"
client.loop_stop()
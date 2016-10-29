#!/usr/bin/python

import paho.mqtt.publish as publish

publish.single("home/bedroom/sunrise/scheduler", payload="GO", hostname="bunker", qos=1)
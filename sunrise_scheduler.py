#!/usr/bin/python

#Simple script that is called by Cron at the scheduled time. Script sends mqtt message that tells the sunrise script to begin the sunrise now.

import paho.mqtt.publish as publish

publish.single("home/bedroom/sunrise/scheduler", payload="GO", hostname="bunker", qos=1)
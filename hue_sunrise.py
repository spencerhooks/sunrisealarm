#!/usr/bin/python

try: import simplejson as json # Try to import simplejson, if not available use json
except ImportError: import json

import time
from phue import Bridge

b = Bridge('192.168.1.193')
lights = b.get_light_objects('name')

with open('color_curves_xy.json') as infile:
    xy_list = json.load(infile)

sunrise_length = 30 # Lenth of sunrise in minutes
color_sleep_length = (sunrise_length*60.0)/len(xy_list) # figure out how long to sleep on each color

b.set_light("Office Hue", {'on' : True, 'bri' : 0, 'xy' : (0.675, 0.322)}) # Turn on the lamp at starting color, lowest brightness

# Loop through the list of colors, increasing brightness
for item, value in enumerate(xy_list, start=0):
    lights["Office Hue"].xy = xy_list[item]
    lights["Office Hue"].brightness = int(item*(254.0/len(xy_list)))
    time.sleep(color_sleep_length)

time.sleep(15*60) # stay on for 15 minutes before shutting off

lights["Office Hue"].on = False # Turn off the lamp

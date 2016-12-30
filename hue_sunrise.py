#!/usr/bin/python

try: import simplejson as json # Try to import simplejson, if not available use json
except ImportError: import json

import time

from phue import Bridge

b = Bridge('192.168.1.217')

lights = b.get_light_objects('name')

with open('color_curves_xy.json') as infile:
    xy_list = json.load(infile)

for item, value in enumerate(xy_list, start=0):
    lights["Office"].xy = xy_list[item]
    print xy_list[item]
    time.sleep(.2)

#!/usr/bin/python

from pyplaybulb import playbulb

bulb = playbulb('CD:B3:4B:0A:AC:E6')
# bulb.on(on_time=.5)
bulb.flash(duration=5, interval=5, wrgb_color='FF000000')
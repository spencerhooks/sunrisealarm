#!/usr/bin/python

import pygatt, array

adapter = pygatt.GATTToolBackend()
value = '0000FF00'

value_data = value.decode("hex")
value_array = array.array('B', value_data)

try:
	adapter.start()
	device = adapter.connect('51:75:4B:0A:AC:E6')
	device.char_write_handle(0x001b, value_array)
finally:
	adapter.stop()
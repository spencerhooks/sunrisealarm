#!/usr/bin/python


from operator import sub
from pyplaybulb import playbulb

bulb = playbulb('51:75:4B:0A:AC:E6')
bulb.on(wrgb_color='000000FF')
# bulb.flash(wrgb_color='FF000000')

bulb.fade_off(duration=300)

# duration = 300
# _current_color = '000000FF'
#
# if duration > 510: duration = 510
# duration = duration/2
#
# # Convert color string into list of hex numbers
# color_list = [int(_current_color[:2], 16), int(_current_color[2:4], 16), int(_current_color[4:6], 16), int(_current_color[6:8], 16)]
#
# # Create list of integers to be subtracted each time through the loop, minimum of 1
# fade_list = [(element/duration) if (element/duration) != 0 else 1 for element in color_list]
# print(fade_list)
# for i in range(duration):
#     color_list = map(sub, color_list, fade_list)  # Subtract the fade amount from the color
#     color_list = [max(0, element) for element in color_list]  # Make sure no color is negative
#     output_list = [hex(element)[2:].zfill(2) for element in color_list] # Format the list to be 2 hex digits
#     output_string = output_list[0] + output_list[1] + output_list[2] + output_list[3] # create output string
#     print(output_string)

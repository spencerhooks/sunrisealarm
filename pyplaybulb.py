#!/usr/bin/python

import time, os

class playbulb(object):

    _is_on = False
    _current_color = ''
    _solid_color = '0x001b'
    _effect = '0x0019'

    # array for red values in the sunrise curve
    red = [0,1,2,4,5,7,8,9,11,12,14,15,17,18,19,21,22,24,25,27,28,29,31,32,34,35,37,38,39,41,42,44,45,47,48,49,51,52,54,55,56,58,59,61,62,64,65,66,68,69,71,72,74,75,76,78,79,81,82,84,85,86,88,89,91,92,94,95,96,98,99,101,102,103,105,106,108,109,111,112,113,115,116,118,119,121,122,123,125,126,128,129,131,132,133,135,136,138,139,141,142,143,145,146,148,149,151,152,153,155,156,158,159,160,162,163,165,166,168,169,170,172,173,175,176,178,179,180,182,183,185,186,188,189,190,192,193,195,196,198,199,200,202,203,205,206,207,209,210,212,213,215,216,217,219,220,222,223,225,226,227,229,230,232,233,235,236,237,239,240,242,243,245,246,247,249,250,252,253,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255]

    # array for green valuves in the sunrise curve
    green = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,11,11,11,12,12,12,13,13,13,14,14,14,15,15,16,16,16,17,17,17,18,18,18,19,19,19,20,20,21,21,21,22,22,22,23,23,23,24,24,24,25,25,26,26,26,27,27,27,28,28,28,29,29,29,30,30,30,31,31,32,32,32,33,33,33,34,34,34,35,35,35,36,36,37,37,37,38,38,38,39,39,39,40,40,40,41,41,42,42,42,43,43,43,44,44,44,45,45,45,46,46,47,47,47,48,48,48,49,49,49,50,50,50,51,51,52,52,52,53,53,53,54,54,54,55,55,55,56,56,57,57,57,58,58,58,59,59,59,60,60,60,61,61,61,62,62,63,63,63,64,64,64,65,65,65,66,66,66,67,67,68,68,68,69,69,69,70,70,70,71,71,71,72,72,73,73,73,74,74,74,75,75,75,76,76,76,77,77,78,78,78,79,79,79,80,80,80,81,81,81,82,82,83,83,83,84,84,84,85,85,85,86,86,86,87,87,88,88,88,89,89,89,90,90,90,91,91,91,92,92,92,93,93,94,94,94,95,95,95,96,96,96,97,97,97,98,98,99,99,99,100,100,100,101,101,101,102,102,102,103,103,104,104,104,105,105,105,106,106,106,107,107,107,108,108,109,109,109,110,110,110,111,111,111,112,112,112,113,113,114,114,114,115,115,115,116,116,116,117,117,117,118,118,119,119,119,120,120,120,121,121,121,122,122,122,123,123,123,124,124,125,125,125,126,126,126,127,127,127,128,128,128,129,129,130,130,130,131,131,131,132,132,132,133,133,133,134,134,135,135,135,136,136,136,137,137,137,138,138,138,139,139,140,140,140,141,141,141,142,142,142,143,143,143,144,144,145,145,145,146,146,146,147,147,147,148,148,148,149,149,150]

    # blue isn't used

    # array for white values in the sunrise curve, filled in below
    white = []

    # make white array values equal to the minimum of the three colors minus 100 (found through trial and error)
    for x in range (0, len(red)):
        if (min(red[x], green[x]) < 100): white.append(0)
        else: white.append(min(red[x], green[x]) - 100)



    def __init__(self, address):
        self.address = address

    def on(self, resume=False, wrgb_color='FFFFFFFF', on_time=0.0):
        if resume == False:
            self.command(self._solid_color, wrgb_color)
            self._current_color = wrgb_color
        elif resume == True:
            self.command(self._solid_color, self.current_color())
        self._is_on = True
        if on_time != 0.0:
            time.sleep(on_time)
            self.off()

    def off(self):
        self.command(self._solid_color, '00000000')
        self._is_on = False

    def flash(self, duration=3.0, interval=1.0, wrgb_color='FFFFFFFF'):
        if interval > duration: raise AttributeError("Duration must be longer than interval")
        num_flashes = int(duration / interval)
        for i in range (0, num_flashes):
            self.on(on_time=(interval/2.0), wrgb_color=wrgb_color)
            time.sleep(interval/2.0)

    def change_color(self, value):
        self.command(self._solid_color, value)
        self._current_color = value

    def sunrise(self, sunrise_length=1800):
        sleep_time = sunrise_length/float(len(self.red))

        print (time.strftime("%H:%M, %d/%m/%y  Started."))
        sys.stdout.flush() # flush the output buffer so the output is immediately sent (useful when redirecting)

        for x in range (0, len(self.white)):
            rise_color = hex(self.white[x])[2:].zfill(2) + hex(self.red[x])[2:].zfill(2) + hex(self.green[x])[2:].zfill(2) + '00'
            self.change_color(value=rise_color)
            time.sleep(sleep_time)

        print (time.strftime("%H:%M, %d/%m/%y  Sunrise complete, now holding."))
        sys.stdout.flush() # flush the output buffer so the output is immediately sent (useful when redirecting)

        time.sleep(sunrise_length/2)
        self.off()
        print (time.strftime("%H:%M, %d/%m/%y  Completed!"))
        sys.stdout.flush() # flush the output buffer so the output is immediately sent (useful when redirecting)

    def is_on(self):
        return self._is_on

    def current_color(self):
        return self._current_color

    def command(self, command, value):
        # print "gatttool -b %s --char-write -a %s -n %s" % (self.address, command, value)
        os.system("gatttool -b %s --char-write -a %s -n %s" % (self.address, command, value))


# add effects, support for simple color names, dimming, add flash N times
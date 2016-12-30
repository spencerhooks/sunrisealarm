#!/usr/bin/python

from noisegen import Player
import time, sox

# p = sox.core
# p.play(["-n", "synth", "brownnoise"])
#
# time.sleep(4)
#
# p.terminate()

p = Player()

p.play()

print "playing stuff"
time.sleep(5)
p.stop()

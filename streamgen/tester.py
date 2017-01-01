#!/usr/bin/python

from streamgen import Player
import time, sox

# p = sox.core
# p.play(["-n", "synth", "brownnoise"])
#
# time.sleep(4)
#
# p.terminate()

p = Player()

p.play(duration=5)

print ("playing stuff")
print (p.is_playing())

time.sleep(6)
# p.stop()

print (p.is_playing())

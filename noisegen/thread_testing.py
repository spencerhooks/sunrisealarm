#!/usr/bin/python

from subprocess import Popen
import os, time
from threading import Thread

# def myplayer():
#     global p
#     p = Popen(['play', '-q', '-n', 'synth', 'brownnoise'])
#     print "running thread"

t = Thread(target = Popen(['play', '-q', '-n', 'synth', 'brownnoise']))
t.daemon = False
t.start()

print (t.is_alive())
time.sleep(5)
target.terminate()
print (t.is_alive())

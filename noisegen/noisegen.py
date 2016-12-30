#!/usr/bin/python
"""
A very simple wrapper around Sound Exchange library (SoX) to provide python playback of the signal
generator function only. Allows input parameters of:
  - Durration of playback in seconds (0=infinite)
  - Signal type (sine, square, triangle, sawtooth, trapezium, exp, [white]noise, tpdfnoise, pinknoise,
    brownnoise, pluck; default=brownnoise)
  - Gain (specified relative to 0dBFS, so should be a negative number)
  - Fadetime (same time used for fadein and fadeout)

Many other parameters can be used with SoX, but are not implemented.

This module Requires that SoX is installed. Please see http://sox.sourceforge.net for more info on SoX.

"""


# from sox import core
from subprocess import Popen
import os

class Player(object):

    def play(self, durration=0, tone='brownnoise', gain=0, fadetime=0):
        """
        Core method, used to play signal.
        """
        fade_stop_time = 0
        if durration == 0: fade_stop_time = None
        global _player
        _player = Popen(['play', '-q', '-n', 'synth', str(durration), tone, 'gain', str(gain), 'fade', 'q', str(fadetime), str(fade_stop_time)])

    def stop(self):
        """
        Function to stop playback. This is only needed when durration is not given or is set to 0 (infinite).
        """
        global _player
        _player.terminate()

#need to check durration and only specificy fadeout if durration is != 0; also might need to check that fadetime is shorter than durration

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

from subprocess import Popen
from threading import Thread, Timer
import os

class Player(object):

    def generate(self, durration=0, tone='brownnoise', gain=0, fadetime=0):
        """
        Method to generate synthetic signal.
        """
        global t
        t = Thread(target = self._send_command, kwargs={'durration': durration, 'tone': tone, 'gain': gain, 'fadetime': fadetime})
        t.start()

    def play(self, durration=0, source='kqed'):
        """
        Method to play mp3 stream.
        """
        global t
        t = Thread(target = self._send_command, kwargs={'tone': source,})
        t.start()

        if durration != 0:
            t2 = Timer(durration, t.stop())
            t2.start()

    def stop(self):
        """
        Method to stop playback. This is only needed when durration is not given or is set to 0 (infinite).
        """
        global _player
        _player.terminate()

    def is_playing(self):
        """
        Method to check status of player. Returns status of thread to indicate activity.
        """
        global t
        return t.is_alive()

    def _send_command(self, durration=0, tone='brownnoise', gain=0, fadetime=0):
        """
        Private method used to send command to SoX player.
        """
        global _player

        if tone == 'kqed':
            _player = Popen(['mpg123', '-q', '-@', 'http://streams.kqed.org/kqedradio.m3u'])
        else:
            is_null = False if durration == 0 else True  # Make sure the fade stop position is null when durration is 0
            _player = Popen(['play', '-q', '-n', 'synth', str(durration), tone, 'gain', str(gain), 'fade', 'q', str(fadetime)] + ['0']*is_null)

# need to figure out how to implement the timer thread so that it stops playback on a different thread
# need to fix when calling is_playing before playing becuase it does not exist to call is_alive() on

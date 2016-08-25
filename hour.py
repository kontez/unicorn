#!/usr/bin/python
# scrolling rainbows and time. uses scrolldisp.py

from scrolldisp import Display
import unicornhat, time

unicornhat.rotation(180)
unicornhat.brightness(0.5)
Display("~R" + time.strftime("%H:%M") + " ~R")

#!/usr/bin/python
# scrolling rainbows and time. uses scrolldisp.py

import unicornhat as u
from scrolldisp import *

u.rotation(180)
u.brightness(0.05)

disp = ScrollDisp("~R" + time.strftime("%H:%M") + " ~R")
disp.start()

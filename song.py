#!/usr/bin/python
# displays the song and artist currently playing on twitch.tv/monstercat
# relies on an homemade script accessible at cigix.noip.me/update.php

from scrolldisp import *
import unicornhat, urllib2, string

unicornhat.rotation(180)
unicornhat.brightness(0.05)

disp = ScrollDisp("~R" + urllib2.urlopen("http://cigix.noip.me/update.php").read() + " ~R")
disp.start(0.03)

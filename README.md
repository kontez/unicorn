# unicorn
Scripts done for the Raspberry Pi Unicorn Hat

hour.py
-------
Uses `scrolldisp.py` to display the time, with rainbows.

rainbow.py
----------
Continuously displays a scrolling rainbow generated using HSV, moving from top to bottom.

rainbow_appear.py
-----------------
Draws a single rainbow, scrolling from top to bottom, using cosine waves.

song.py
-------
Uses `scrolldisp.py` to display what song is currently playing on twitch.tv/monstercat,
using a private external script at cigix.noip.me/update.php

scrolldisp.py
-------------
A library to make text scroll on the Unicorn. Due to the way I implemented it,
the default rotation is upside down, USB and Ethernet port pointing upwards.

Contains a single class, ScrollDisp. Use

    import scrolldisp
    disp = scrolldisp.ScrollDisp()

or

    from scrolldisp import *
    disp = ScrollDisp()

**Functions**

    ScrollDisp(text)
  
Creates a new `ScrollDisp` object and sets its buffer to `text` (optional).

    disp.set_text(text, color)

Clears and sets the buffer for `disp` to `text`. `color` is a standard unicorn RGB tuple, default is (255,255,255) (white).

    disp.start(delay)
  
Makes the buffer for `disp` scroll on unicorn. `time.sleep(delay)` is called between each frame.
Default delay is 0.1 and scrolls text smoothly.

**Supported characters**

* Uppercase and lowercase letters
* All digits
* Special characters: `!'(),-.:[]_` and space
* Escape sequences: Implementation allows for escape sequences starting with `~` (tilde). Currently, the only escape sequence implemented is:
  * `~R`: Draws a rainbow generated using cosine waves (see `rainbow_appear.py`)

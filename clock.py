#!/usr/bin/python
# my own attempt at displaying a clock. WIP

import unicornhat as u
import time, math

u.brightness(0.05)

def line(x1,y1,x2,y2,color=(0,0,0)):
    l = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    dx = (x2-x1) / l
    dy = (y2-y1) / l
    r,g,b = color
    u.set_pixel(int(x1),int(y1),r,g,b)
    while (x1,y1) != (x2,y2):
        x1 += dx
        y1 += dy
        u.set_pixel(int(x1),int(y1),r,g,b)

def circle(color=(0,0,0)):
    line(0.0,2.0,0.0,5.0,color)
    line(2.0,0.0,5.0,0.0,color)
    line(7.0,2.0,7.0,5.0,color)
    line(2.0,7.0,5.0,7.0,color)
    r,g,b = color
    u.set_pixel(1,1,r,g,b)
    u.set_pixel(1,6,r,g,b)
    u.set_pixel(6,6,r,g,b)
    u.set_pixel(6,1,r,g,b)

#circle((0,255,255))

n = 0.0
while n < 2 * math.pi:
    u.set_pixel(int(round(3.5 + 3.9 * math.cos(n))), int(round(3.5 + 3.9 * math.sin(n))), 255, 0, 128)
    n += 0.1
u.show()
time.sleep(2)
exit()
    

while True:
    currenttime = time.localtime()
    currenthour = currenttime.tm_hour
    currentmin  = currenttime.tm_min
    currentsec  = currenttime.tm_sec

    ah = (0.5 - currenthour / 30.0) * math.pi

    circle()

    u.show()
    time.sleep(1)
    u.clear()


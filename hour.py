#!/usr/bin/python
# scrolling rainbows and text. used to display the time

import unicornhat as u
import time, math

columns = []
u.rotation(180)
u.brightness(0.05)

def append_rainbow():
    for x in range(8):
        r = int((math.cos(x * math.pi / 4) + 1) * 127)
        g = int((math.cos((x - 8.0 / 3.0) * math.pi / 4) + 1) * 127)
        b = int((math.cos((x + 8.0 / 3.0) * math.pi / 4) + 1) * 127)
        columns.append([(r,g,b) for i in range(8)])

def append_space(n=1):
    for x in range(n):
        columns.append([(0,0,0) for i in range(8)])

def append_buffer():
    append_space(8)

def append_letter(char, C=(255,255,255)):
    append_space()
    z = (0,0,0)
    if char == ' ':
        append_space()
    elif char == ':':
        columns.append([z,C,z,z,C,z,z,z])
    elif char == '0':
        columns.append([z,z,C,C,C,C,z,z])
        columns.append([z,C,z,z,z,z,C,z])
        columns.append([z,C,z,z,z,z,C,z])
        columns.append([z,z,C,C,C,C,z,z])
    elif char == '1':
        columns.append([z,C,z,z,z,C,z,z])
        columns.append([z,C,C,C,C,C,C,z])
        columns.append([z,C,z,z,z,z,z,z])
    elif char == '2':
        columns.append([z,C,z,z,z,C,z,z])
        columns.append([z,C,C,z,z,z,C,z])
        columns.append([z,C,z,C,z,z,C,z])
        columns.append([z,C,z,z,C,C,z,z])
    elif char == '3':
        columns.append([z,z,C,z,z,z,C,z])
        columns.append([z,C,z,z,z,z,C,z])
        columns.append([z,C,z,z,C,z,C,z])
        columns.append([z,z,C,C,z,C,C,z])
    elif char == '4':
        columns.append([z,z,z,z,C,C,C,z])
        columns.append([z,z,z,z,C,z,z,z])
        columns.append([z,z,z,z,C,z,z,z])
        columns.append([z,C,C,C,C,C,C,z])
    elif char == '5':
        columns.append([z,z,C,z,C,C,C,z])
        columns.append([z,C,z,z,C,z,C,z])
        columns.append([z,C,z,z,C,z,C,z])
        columns.append([z,z,C,C,z,z,C,z])
    elif char == '6':
        columns.append([z,z,C,C,C,C,z,z])
        columns.append([z,C,z,z,C,z,C,z])
        columns.append([z,C,z,z,C,z,C,z])
        columns.append([z,z,C,C,z,z,z,z])
    elif char == '7':
        columns.append([z,z,z,z,z,z,C,z])
        columns.append([z,C,C,z,z,z,C,z])
        columns.append([z,z,z,C,C,z,C,z])
        columns.append([z,z,z,z,z,C,C,z])
    elif char == '8':
        columns.append([z,z,C,C,z,C,z,z])
        columns.append([z,C,z,z,C,z,C,z])
        columns.append([z,C,z,z,C,z,C,z])
        columns.append([z,z,C,C,z,C,z,z])
    elif char == '9':
        columns.append([z,z,z,z,C,C,z,z])
        columns.append([z,C,z,C,z,z,C,z])
        columns.append([z,C,z,C,z,z,C,z])
        columns.append([z,z,C,C,C,C,z,z])

def append_string(text, color=(255,255,255)):
    for i in text:
        append_letter(i, color)

append_buffer()
append_rainbow()
append_string(time.strftime("%H:%M"))
append_space()
append_rainbow()
append_buffer()

for x in range(len(columns) - 8):
    u.set_pixels(columns[x:x+8])
    u.show()
    time.sleep(0.1)


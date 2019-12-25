import json
from tkinter import *

def toHex(r, g, b):
	return '#' + hex(r)[2:] + hex(g)[2:] + hex(b)[2:]

file = open('regions.json')
coordinates = json.load(file)
file.close()

top = Tk()

C = Canvas(top, bg=toHex(50, 150, 100), width=1920, height=1080)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")
line = C.create_line(10, 10, 200, 200, fill='white')
C.pack()
top.mainloop()

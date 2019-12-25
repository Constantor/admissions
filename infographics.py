import json
from tkinter import *
from math import pi, log, tan

from analyze import out, got


def toHex(r, g, b):
	return '#' + hex(r)[2:] + hex(g)[2:] + hex(b)[2:]

def radians(alpha):
	return pi * alpha / 180

file = open('regions.json')
coordinates = json.load(file)
file.close()

top = Tk()

canvas = Canvas(top, bg='#ffffff', width=3400, height=1800)

# lines = []
polygons = []
zoom = 4.75
x0 = 3750
y0 = 900
x = lambda l: (128 / pi) * 2 ** zoom * (l + pi) - x0
y = lambda phi: (128 / pi) * 2 ** zoom * (pi - log(tan(pi / 4 + phi / 2))) - y0
for region in coordinates:
	points = coordinates[region]['0']
	coords = []
	for i in range(len(coordinates[region]['0']) - 1):
		coords.extend([x(radians(points[i][1])), y(radians(points[i][0])), x(radians(points[i + 1][1])), y(radians(points[i + 1][0]))])
		# lines.append(canvas.create_line(x(radians(points[i][1])), y(radians(points[i][0])), x(radians(points[i + 1][1])), y(radians(points[i + 1][0])), fill='#000000', width=2))
	polygons.append(canvas.create_polygon(coords, outline='#000000', fill='#eeeeee', width=2))

canvas.pack()
top.mainloop()

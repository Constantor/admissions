import json
from tkinter import *
from math import pi, log, tan

from analyze import out, got
from regions import regions

def round(x):
	frac = x - int(x)
	if frac < 0.5:
		return int(x)
	return int(x) + 1

def toHex(r, g, b):
	hr = hex(r)[2:]
	if len(hr) == 1:
		hr = '0' + hr
	hg = hex(g)[2:]
	if len(hg) == 1:
		hg = '0' + hg
	hb = hex(b)[2:]
	if len(hb) == 1:
		hb = '0' + hb
	return '#' + hr + hg + hb

def radians(alpha):
	return pi * alpha / 180

file = open('regions.json')
coordinates = json.load(file)
file.close()

top = Tk()

canvas = Canvas(top, bg='#0000ff', width=3400, height=1800)

# lines = []
polygons = []
zoom = 4.75
x0 = 3750
y0 = 900
x = lambda l: (128 / pi) * 2 ** zoom * (l + pi) - x0
y = lambda phi: (128 / pi) * 2 ** zoom * (pi - log(tan(pi / 4 + phi / 2))) - y0
maxOut = max(out)
minOut = min(out)
maxGot = max(got)
minGot = min(got)
for region in coordinates:
	points = coordinates[region]['0']
	coords = []
	for i in range(len(coordinates[region]['0']) - 1):
		coords.extend([x(radians(points[i][1])), y(radians(points[i][0])), x(radians(points[i + 1][1])), y(radians(points[i + 1][0]))])
		# lines.append(canvas.create_line(x(radians(points[i][1])), y(radians(points[i][0])), x(radians(points[i + 1][1])), y(radians(points[i + 1][0])), fill='#000000', width=2))
	shift = 0
	if region in regions:
		shift = round(255 * ((out[regions[region]] - minOut) / (maxOut - minOut)))
	polygons.append(canvas.create_polygon(coords, outline='#000000', fill=toHex(shift, 255 - shift, 0), width=2))

canvas.pack()
top.mainloop()

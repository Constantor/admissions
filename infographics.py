import json
from tkinter import *
from math import pi, log, tan
from PIL import Image

from analyze import out, got
from regions import regions

def round(x):
	frac = x - int(x)
	if frac < 0.5:
		return int(x)
	sign = -1 if x < 0 else 1
	if sign == 1:
		return int(x) + 1
	return int(x) - 1

def toHex(r, g=None, b=None):
	if g == None and b == None:
		return toHex(r[0], r[1], r[2])
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

empty = (238, 238, 238)
weak = (166, 226, 46)
powerful = (249, 38, 114)

top = Tk()

canvas = Canvas(top, bg='#ffffff', width=3750, height=2050)

canvas.create_text(3600, 1950, fill='#000000', font='Courier 20', text='— 0    ')
canvas.create_text(3600, 1800, fill='#000000', font='Courier 20', text='— 1-179')

boxW = 175
boxH = 75
box0x = 3300
box0y = 1915
zeroBox = canvas.create_polygon([box0x, box0y, box0x + boxW, box0y, box0x + boxW, box0y + boxH, box0x, box0y + boxH], outline='#000000', fill=toHex(empty), width=2)
boxW = 175
boxH = 75
box0x = 3300
box0y = 1765
rangeBoxL = canvas.create_polygon([box0x, box0y, box0x + boxW / 2, box0y, box0x + boxW / 2, box0y + boxH, box0x, box0y + boxH], outline='#000000', fill=toHex(weak), width=2)
rangeBoxR = canvas.create_polygon([box0x + boxW / 2, box0y, box0x + boxW, box0y, box0x + boxW, box0y + boxH, box0x + boxW / 2, box0y + boxH], outline='#000000', fill=toHex(powerful), width=2)

# lines = []
polygons = []
zoom = 4.9
x1 = lambda l: (128 / pi) * 2 ** zoom * (l + pi)
y1 = lambda phi: (128 / pi) * 2 ** zoom * (pi - log(tan(pi / 4 + phi / 2)))
x0 = x1(radians(15))
y0 = y1(radians(78)) - 50
x = lambda l: x1(l) - x0
y = lambda phi: y1(phi) - y0
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
	shift = -1
	if region in regions:
		shift = (out[regions[region]] - minOut) / (maxOut - minOut)
	toFill = toHex(empty)
	if shift != -1:
		toFill = toHex([weak[i] + round(shift * (powerful[i] - weak[i])) for i in range(3)])
	polygons.append(canvas.create_polygon(coords, outline='#000000', fill=toFill, width=2))

canvas.pack()
canvas.update()

filename = 'out'
canvas.postscript(file=filename + '.ps')
img = Image.open(filename + '.ps')
img.save(filename + '.png', 'png')

top.mainloop()

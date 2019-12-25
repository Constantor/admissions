import json

file = open('regions.json')
coordinates = json.load(file)
file.close()

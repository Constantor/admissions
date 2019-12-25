import shapefile

sf = shapefile.Reader('regions2010_wgs.shp')

print(set(sf.shape(1114).points) == set(sf.shape(1124).points))

for a in sf.shape(1124).points:
	print('[' + str(a[1]) + ', ' + str(a[0]) + '],')

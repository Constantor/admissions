from admission import admissions

universities = set()
for year in admissions:
	for subject in admissions[year]:
		for university in admissions[year][subject]:
			universities.add(university)

for university in universities:
	print(university)

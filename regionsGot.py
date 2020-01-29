from regions import regions, nRegions, aliases
from admission import admissions
from universities import universityRegions, universities
from collections import Counter

cntGot = Counter()

for season in admissions:
	if season != '20182019':
		continue
	for subject in admissions[season]:
		if subject != 'mathematics':
			continue
		for university in admissions[season][subject]:
			for course in admissions[season][subject][university]:
				cntGot[universityRegions[university.lower()]] += len(admissions[season][subject][university][course])

out = sorted(list(cntGot.items()), reverse=True, key=lambda x: x[1])
for o in out:
	print(list(aliases[regions[o[0].lower()]])[0] + '\t' + str(o[1]))

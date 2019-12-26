from collections import Counter
import pickle
from admission import admissions
from universities import universities, universityRegions
from regions import regions, aliases, nRegions

file = open('contests.pickle', 'rb')
contests = pickle.load(file)
file.close()

out = [0] * nRegions
got = [0] * nRegions

for subject in contests:
	for season in contests[subject]:
		for contestant in contests[subject][season]:
			out[regions[contestant['region']]] += 1

for season in admissions:
	for subject in admissions[season]:
		for university in admissions[season][subject]:
			got[regions[universityRegions[university]]] += sum([len(admissions[season][subject][university][direction]) for direction in admissions[season][subject][university]])

universitiesCnt = Counter()
for season in admissions:
	for subject in admissions[season]:
		for university in admissions[season][subject]:
			universitiesCnt[university] += sum([len(admissions[season][subject][university][direction]) for direction in admissions[season][subject][university]])

sortedIds = sorted(list(range(nRegions)), key=lambda i: out[i], reverse=True)
for i in range(nRegions):
	print(aliases[sortedIds[i]].pop() + '\t' + str(out[sortedIds[i]]) + '\t' + str(got[sortedIds[i]]))
print()
sortedUniversities = sorted(list(universitiesCnt.keys()), key=lambda university: universitiesCnt[university], reverse=True)
for university in sortedUniversities:
	print(university + '\t' + str(universitiesCnt[university]))

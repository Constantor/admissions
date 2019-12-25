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
			got[regions[universityRegions[university]]] += len(admissions[season][subject][university])

sortedIds = sorted(list(range(nRegions)), key=lambda i: out[i], reverse=True)
for i in range(nRegions):
	print(aliases[sortedIds[i]].pop() + '\t' + str(out[sortedIds[i]]) + '\t' + str(got[sortedIds[i]]))

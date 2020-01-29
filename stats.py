from regions import regions, nRegions, aliases
from admission import admissions
import pickle
from collections import Counter


file = open('contests.pickle', 'rb')
contests = pickle.load(file)
file.close()

cnt = Counter()
for subject in contests:
	if subject != 'programming':
		continue
	for season in contests[subject]:
		if season != '20172018':
			continue
		for contestant in contests[subject][season]:
			if (contestant['type'].lower() == 'призёр' or contestant['type'].lower() == 'призер' or contestant['type'].lower() == 'победитель' or 'диплом' in contestant['type'].lower()) and contestant['grade'] == 11:
				cnt[regions[contestant['region'].lower()]] += 1

out = sorted(list(cnt.items()), reverse=True, key=lambda x: x[1])
for o in out:
	print(list(aliases[o[0]])[0] + '\t' + str(o[1]))

import pickle

file = open('contests.pickle', 'rb')
contests = pickle.load(file)
file.close()

regions = set()
for subject in contests:
	for season in contests[subject]:
		for contestant in contests[subject][season]:
			regions.add(contestant['region'])

for region in regions:
	print(region)

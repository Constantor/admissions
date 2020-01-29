from admission import admissions
import pickle


file = open('contests.pickle', 'rb')
contests = pickle.load(file)
file.close()

contesters = set()
applicants = set()

for subject in contests:
	for season in contests[subject]:
		if season != '20182019':
			continue
		for contestant in contests[subject][season]:
			if (contestant['type'].lower() == 'призёр' or contestant['type'].lower() == 'призер' or contestant['type'].lower() == 'победитель' or 'диплом' in contestant['type'].lower()) and contestant['grade'] == 11:
				contesters.add(contestant['last_name'] + ' ' + contestant['first_name'] + ' ' + contestant['middle_name'])

for season in admissions:
	if season != '20182019':
		continue
	for subject in admissions[season]:
		for university in admissions[season][subject]:
			for course in admissions[season][subject][university]:
				for applicant in admissions[season][subject][university][course]:
					applicants.add(applicant)

print(len(contesters))
print(len(applicants))
print(len(contesters) - len(applicants))
print((contesters - applicants).pop())

from contests import contests

students = set()

for subject in contests.values():
	for year, yearcontent in subject.items():
		if year == '20162017':
			continue
		for student in yearcontent:
			students.add((student['last_name'], student['first_name'], student['middle_name']))

print(len(students))

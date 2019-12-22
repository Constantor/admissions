import os

from admission import admissions

subjects = ('mathematics', 'programming')
seasons = ('20172018', '20182019')

for season in seasons:
	for subject in subjects:
		for university in admissions[season][subject]:
			for direction in admissions[season][subject][university]:
				student = admissions[season][subject][university][direction].pop().replace(' ', '+')
				os.system('chromium https://www.google.com/search?q=' + student + '+приказ+о+зачислении+' + university.replace(' ', '+') + '+' + direction.replace(' ', '+') + '+' + season[-4:])

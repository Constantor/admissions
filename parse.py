import pickle


class Parse:
	@staticmethod
	def programming(raw):
		contestantsRaw = [line.strip().split('\t') for line in raw.strip().split('\n')]
		contestants = [dict() for __ in range(len(contestantsRaw))]
		for i, current in enumerate(contestantsRaw):
			contestants[i]['place'] = int(current[0])
			braceOpen = current[1].index('(')
			braceClose = current[1].index(')')
			contestants[i]['region'], contestants[i]['grade'] = current[1][braceOpen + 1:braceClose].strip().split(', ')
			contestants[i]['grade'] = int(contestants[i]['grade'])
			contestants[i]['last_name'], contestants[i]['first_name'], contestants[i]['middle_name'] = current[1][:braceOpen - 1].strip().split(' ')
			contestants[i]['score'] = int(current[-3])
			contestants[i]['type'] = current[-1]
		return contestants

	@staticmethod
	def mathematics(raw, is2017=False):
		contestantsRaw = [line.strip().split('\t') for line in raw.strip().split('\n')]
		contestants = [dict() for __ in range(len(contestantsRaw))]
		for i, current in enumerate(contestantsRaw):
			contestants[i]['place'] = int(current[0])
			if current[1].count(' ') == 1:
				current[1] += ' -'
			contestants[i]['last_name'], contestants[i]['first_name'], contestants[i]['middle_name'] = current[1].split(' ')
			contestants[i]['grade'] = int(current[2])
			contestants[i]['school'] = current[3 if not is2017 else 4]
			contestants[i]['region'] = current[4 if not is2017 else 4]
			contestants[i]['score'] = int(current[-2])
			contestants[i]['type'] = current[-1].capitalize()
		return contestants

	@staticmethod
	def physics(raw):
		contestantsRaw = [line.strip().split('\t') for line in raw.strip().split('\n')]
		contestants = [dict() for __ in range(len(contestantsRaw))]
		for i, current in enumerate(contestantsRaw):
			contestants[i]['place'] = int(current[0])
			if current[1].count(' ') == 1:
				current[1] += ' -'
			contestants[i]['last_name'], contestants[i]['first_name'], contestants[i]['middle_name'] = current[1].split(' ')
			contestants[i]['grade'] = 11
			contestants[i]['school'] = current[2]
			contestants[i]['type'] = current[3]
			contestants[i]['region'] = 'Москва'
		return contestants

	@staticmethod
	def sociology(raw):
		pass

	@staticmethod
	def history(raw):
		pass


if __name__ == '__main__':
	subjects = {'programming', 'mathematics'}
	seasons = {'20162017', '20172018', '20182019'}

	file = open('contests.pickle', 'wb+')
	result = {}
	for subject in subjects:
		result[subject] = {}
		for season in seasons:
			if subject == 'programming':
				result[subject][season] = Parse.programming(open('unparsed/programming' + season + '.txt').read())
			elif subject == 'mathematics':
				result[subject][season] = Parse.mathematics(open('unparsed/mathematics' + season + '.txt').read()) if not season == '20162017' else Parse.mathematics(open('unparsed/mathematics' + season + '.txt').read(), True)

	pickle.dump(result, file)
	file.close()

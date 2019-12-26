universities = {
	'Москва': {
		'РЭУ',
		'МГИМО',
		'РГУ нефти и газа (НИУ) имени И.М. Губкина',
		'ВШЭ',
		'МИЭП',
		'МГУ',
	},
	'Московская область': {
		'МФТИ',
	},
	'Санкт-Петербург': {
		'ВШЭ (Санкт-Петербург)',
		'ИТМО',
		'СПб Горный',
		'СПбГУТ им. Бонч-Бруевича',
		'СПбГУ',
	},
	'Воронежская область': {
		'ВГУ',
	},
	'Нижегородская область': {
		'ВШЭ (Нижний Новгород)'
	},
	'Свердловская область': {
		'УПК-МЦК'
	},
	'Республика Татарстан': {
		'КФУ',
	}
}

keys = list(universities.keys())
for key in keys:
	if key != key.lower():
		universities[key.lower()] = universities[key]
		universities.pop(key)

universityRegions = dict()
for region in universities:
	for university in universities[region.lower()]:
		universityRegions[university] = region.lower()

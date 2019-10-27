import pickle


file = open('contests.pickle', 'rb')
contests = pickle.load(file)
file.close()

for contestant in contests['programming']['20182019']:
    if contestant['grade'] == 11:
        print(contestant['place'], contestant['last_name'], contestant['first_name'], contestant['middle_name'], contestant['region'], contestant['type'])

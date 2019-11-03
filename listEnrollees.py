import pickle

file = open('contests.pickle', 'rb')
contests = pickle.load(file)
file.close()

subject = 'programming'
season = '20172018'

for contestant in contests[subject][season]:
    if contestant['grade'] == 11:
        print(contestant['place'], contestant['last_name'], contestant['first_name'], contestant['middle_name'], contestant['region'], contestant['type'])

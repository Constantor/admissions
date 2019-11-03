import pickle
import os

file = open('contests.pickle', 'rb')
contests = pickle.load(file)
file.close()

subject = 'programming'
season = '20172018'

for contestant in contests[subject][season]:
    if contestant['grade'] == 11 and 27 <= int(contestant['place']):
        os.system('chromium https://www.google.com/search?q=' + contestant['last_name'] + '+' + contestant['first_name'] + '+' + contestant['middle_name'] + '+приказ+о+зачислении+2018')
        print(contestant['place'], contestant['last_name'], contestant['first_name'], contestant['middle_name'], contestant['region'], contestant['type'])

import pickle
import os

file = open('contests.pickle', 'rb')
contests = pickle.load(file)
file.close()

subject = 'history'
season = '20182019'

for contestant in contests[subject][season]:
    if contestant['grade'] == 11:
        os.system('chromium https://www.google.com/search?q=' + contestant['last_name'] + '+' + contestant['first_name'] + '+' + contestant['middle_name'] + '+приказ+о+зачислении+' + season[-4:])
        print(contestant['place'], contestant['last_name'], contestant['first_name'], contestant['middle_name'], contestant['region'], contestant['type'])

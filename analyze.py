import pickle
from admission import admissions

file = open('contests.pickle', 'rb')
contests = pickle.load(file)
file.close()



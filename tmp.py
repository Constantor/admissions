import pickle


file = open('contests.pickle', 'rb')
contests = pickle.load(file)
file.close()

print(contests['programming']['20182019'])

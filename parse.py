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


if __name__ == '__main__':
    file = open('contests.pickle', 'wb+')
    result = {
        'programming': {
            '20182019': Parse.programming(open('unparsed/programming20182019.txt').read())
        }
    }
    pickle.dump(result, file)
    file.close()
import string


class WordChecker:
    def __init__(self, word):
        self.word = word.upper()


    def word_checker(self):
        with open('PossibleWords.txt', encoding='utf-8') as f:
            dic = {}
            for words in f:
                bank = f.readlines()
                for idx, ele in enumerate(bank):
                    bank[idx] = ele.replace('\n', '')
            for i, j in enumerate(bank):
                dic[j] = i

        if self.word in dic:
            return "Valid"
        else:
            return "Invalid"



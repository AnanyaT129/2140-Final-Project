# class containing functions to do with an entered word
#  - check word validity
#  - get word score
#  - add word score to player

global scoreboard
scoreboard = [[3,1,2,1,3], [1,1,1,1,1], [3,1,3,1,3], [1,1,1,1,1], [3,1,2,1,3]]
global letter_value 
letter_value = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1., "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10}

class WordClass:
    def __init__(self, word, start, direction, player):
        self.word = word
        self.starting_point = start
        self.direction = direction
        self.player = player

    # check word is in dictionary
    
    # check word is in a valid location/length

    # check word uses the existing letters on the board properly

    # check word is not a repeated word

    # check word is valid
    def valid_word(self):
        # if above functions all return true:
            return True
        # else:
            return False
    
    def calculate_points(self):
        list_of_letters = [char for char in self.word.upper()]
        sum = 0
        try:
            if self.direction == "down":
                for x in range(len(self.word)):
                    sum += (scoreboard[self.starting_point[0]+x][self.starting_point[1]] * letter_value.get(list_of_letters[x]))
            else:
                for x in range(len(self.word)):
                    sum += (scoreboard[self.starting_point[0]][self.starting_point[1]+x] * letter_value.get(list_of_letters[x]))
            
            return sum
        except:
            return "Invalid"

word1 = WordClass("word", (0,0), "down", 1)
word2 = WordClass("word", (0,0), "right", 2)
word3 = WordClass("word", (2,2), "right", 2)
print(word1.calculate_points()) #18
print(word2.calculate_points()) #17
print(word3.calculate_points()) #"Invalid"
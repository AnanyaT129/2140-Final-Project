# all classes used in the Scrabble Game

import random
import numpy as np

# global variables
global BOARD_DIMENSION
BOARD_DIMENSION = 5
global letter_value 
letter_value = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1., "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10}

# PlayerClass
# class containing functions to do with a player
#  - Update score
#  - Get score
#  - Remove letters
#  - Replenish letters
#  - Get letters

class PlayerClass:
    def __init__(self, name, bag):
        self.name = name
        self.score = 0
        self.letters = []
        self.skips = 0
        self.replenish_letters(bag)
    
    def update_score(self, points):
        self.score = self.score + points
    
    def get_score(self):
        return self.score
    
    def replenish_letters(self, bag):
        x = 7 - len(self.letters)
        for y in range(x):
            self.letters.append(bag.remove_tile())
    
    def get_letters(self):
        return self.letters

# BagClass
# class containing functions to do with the bag of letters
#  - initializes bag
#  - gets number of tiles in bag
#  - removes letter from bag

class BagClass:
    def __init__(self):
        self.bag = []
        self.initialize()

    def initialize(self):
        self.bag.extend(["A"] * 9)
        self.bag.extend(["B"] * 2)
        self.bag.extend(["C"] * 2)
        self.bag.extend(["D"] * 4)
        self.bag.extend(["E"] * 12)
        self.bag.extend(["F"] * 2)
        self.bag.extend(["G"] * 3)
        self.bag.extend(["H"] * 2)
        self.bag.extend(["I"] * 9)
        self.bag.extend(["J"] * 1)
        self.bag.extend(["K"] * 1)
        self.bag.extend(["L"] * 4)
        self.bag.extend(["M"] * 2)
        self.bag.extend(["N"] * 6)
        self.bag.extend(["O"] * 8)
        self.bag.extend(["P"] * 2)
        self.bag.extend(["Q"] * 1)
        self.bag.extend(["R"] * 6)
        self.bag.extend(["S"] * 4)
        self.bag.extend(["T"] * 6)
        self.bag.extend(["U"] * 4)
        self.bag.extend(["V"] * 2)
        self.bag.extend(["W"] * 2)
        self.bag.extend(["X"] * 1)
        self.bag.extend(["Y"] * 2)
        self.bag.extend(["Z"] * 1)
        self.bag.extend(["BLANK"] * 2)

        random.shuffle(self.bag)

    def remove_tile(self):
        removed = self.bag[-1]
        self.bag.pop()
        return removed
        
    def get_bag_size(self):
        return len(self.bag)

# BoardClass
# class containing functions to do with the game board
#  - initializes score multiples
#  - places word on board

class BoardClass:
    def __init__(self):
        self.board_letters = np.zeros((BOARD_DIMENSION, BOARD_DIMENSION), dtype=int).tolist()
        self.board_scores = np.ones((BOARD_DIMENSION, BOARD_DIMENSION), dtype=int)
        self.guesses = []
        self.set_scores()
    
    def set_scores(self):
        self.board_scores[0][0] = 3
        self.board_scores[0][2] = 2
        self.board_scores[0][4] = 3
        self.board_scores[2][0] = 3
        self.board_scores[2][2] = 3
        self.board_scores[2][4] = 3
        self.board_scores[4][0] = 3
        self.board_scores[4][2] = 2
        self.board_scores[4][4] = 3

    def place_word(self, word, direction, start):
        try:
            list_of_letters = [char for char in word.upper()]
            if direction == "down":
                for x in range(len(word)):
                    self.board_letters[start[0] + x][start[1]] = list_of_letters[x]
            elif direction == "right":
                for x in range(len(word)):
                    self.board_letters[start[0]][start[1] + x] = list_of_letters[x]
        except IndexError:
            print("The word you inputted is either too long or the starting point is invalid.")
    
    def get_guesses(self):
        return self.guesses
    
    def get_scoreboard(self):
        return self.board_scores

# WordClass
# class containing functions to do with an entered word
#  - check word validity
#  - get word score
#  - add word score to player

class WordClass:
    def __init__(self, word, start, direction, player):
        self.word = word.upper()
        self.starting_point = start
        self.direction = direction
        self.player = player

    # check word is in dictionary
    def word_checker(self):
        with open('PossibleWords.txt', encoding='utf-8') as f:
            dic = {}
            
            #adds all the words in scrabble from the txt file into a dictionary
            for words in f:                                         
                bank = f.readlines()
                for idx, ele in enumerate(bank):
                    bank[idx] = ele.replace('\n', '')
            for i, j in enumerate(bank):
                dic[j] = i
                
            #if the word is in the dictionary created above the function returns valid
        if self.word in dic:
            return True
        else:
            return False

    # check word uses the existing letters on the board properly

    # check word is not a repeated word
    def check_repeat(self, board):
        if self.word in board.get_guesses():
            return False
        else:
            return True

    # check word is valid
    def valid_word(self, board):
        if WordClass.word_checker(self.word) and WordClass.check_repeat(board):
            return True
        else:
            return False
    
    def calculate_points(self, board):
        list_of_letters = [char for char in self.word.upper()]
        sum = 0
        scoreboard = board.get_scoreboard()
        try:
            if self.direction == "down":
                for x in range(len(self.word)):
                    sum += (scoreboard[self.starting_point[0]+x][self.starting_point[1]] * letter_value.get(list_of_letters[x]))
            else:
                for x in range(len(self.word)):
                    sum += (scoreboard[self.starting_point[0]][self.starting_point[1]+x] * letter_value.get(list_of_letters[x]))
            
            return sum
        except:
            return 0
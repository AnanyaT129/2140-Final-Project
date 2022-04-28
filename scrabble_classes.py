# all classes used in the Scrabble Game

import random
import numpy as np
import math

# global variables
global letter_value
letter_value = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3,
                "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1., "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4,
                "Z": 10}

# PlayerClass
# class containing functions to do with a player
#  - Update score
#  - Get score
#  - Remove letters
#  - Replenish letters
#  - Get letters

class PlayerClass:
    '''
    Represent a player in the game of scrabble

    Class variables:
    name (String) -- the player's name
    score (Natural Number) -- the player's score
    letters (List of Characters) -- the player's current hand of 7 letters
    skips (Natural Number) -- the number of skipped turns the player has taken
    '''
    def __init__(self, name, bag):
        '''
        Constructor
        
        Keyword Arguments:
        name (String) -- the player's name
        bag (BagClass) -- the bag of letters in the game
        '''
        self.name = name
        self.score = 0
        self.letters = []
        self.skips = 0
        self.replenish_letters(bag)

    def update_score(self, points):
        '''
        Add the incomming points to the existing score
        
        Keyword Arguments:
        points (Positive Integer) -- the incoming points
        '''
        self.score += points

    def get_score(self):
        '''Return the player's score'''
        return self.score

    def replenish_letters(self, bag):
        '''
        Add letters to the player's hand until they have 7 total
        
        Keyword Arguments:
        bag (BagClass) -- the bag of letters in the game
        '''
        x = 7 - len(self.letters)
        for y in range(x):
            self.letters.append(bag.remove_tile())

    def get_letters(self):
        '''Return the player's hand'''
        return self.letters

    def remove_letter(self, letter):
        '''Remove the specified letter from the player's hand'''
        self.letters.remove(letter)


# BagClass
# class containing functions to do with the bag of letters
#  - initializes bag
#  - gets number of tiles in bag
#  - removes letter from bag

class BagClass:
    '''
    Represent the bag of letters in the game of scrabble

    Class variables:
    bag (List of Strings) -- a list representing all the letters
    '''
    def __init__(self):
        '''Constructor'''
        self.bag = []
        self.initialize()
    
    def initialize(self):
        '''Add all the letters to the bag and randomize the order'''
        self.bag.extend(["A"] * 10)
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
        self.bag.extend(["U"] * 5)
        self.bag.extend(["V"] * 2)
        self.bag.extend(["W"] * 2)
        self.bag.extend(["X"] * 1)
        self.bag.extend(["Y"] * 2)
        self.bag.extend(["Z"] * 1)

        random.shuffle(self.bag)

    def remove_tile(self):
        '''Remove a tile from the bag and return it'''
        removed = self.bag[-1]
        self.bag.pop()
        return removed

    def get_bag_size(self):
        '''Return the number of letters in the bag'''
        return len(self.bag)


# BoardClass
# class containing functions to do with the game board
#  - initializes score multiples
#  - places word on board

class BoardClass:
    '''
    Represent the game board in the game of scrabble

    Class variables:
    board_dimension (Positive Integer) -- the length of a side of the square board
    board_letters (List of Lists of Characters) -- square matrix representing letters placed on the board
    board_scores (NumPy Array) -- square NumPy array with the score weight of each square
    guesses (List of Strings) -- list of words guessed in the game so far
    '''
    def __init__(self):
        '''Constructor'''
        self.board_dimension = 15
        self.board_letters = np.zeros((self.board_dimension, self.board_dimension), dtype=int).tolist()
        self.board_scores = np.ones((self.board_dimension, self.board_dimension), dtype=int)
        self.guesses = []
        self.set_scores()

    def set_scores(self):
        '''Set the locations of the 2 and 3 weight squares in the board'''
        # constants
        dim = self.board_dimension - 1
        half = math.ceil(dim / 2)
        fourth = math.ceil (half / 2)

        # diagonals
        for x in range(self.board_dimension):
            self.board_scores[x][x] = 2
            self.board_scores[dim - x][x] = 2

        # edges
        self.board_scores[half][0] = 3
        self.board_scores[0][half] = 3
        self.board_scores[dim][half] = 3
        self.board_scores[half][dim] = 3

        for x in range(fourth):

            # top triangle
            self.board_scores[half - x][0 + fourth - x] = 3
            self.board_scores[half + x][0 + fourth - x] = 3

            # left triangle
            self.board_scores[0 + fourth - x][half - x] = 3
            self.board_scores[0 + fourth - x][half + x] = 3

            # right triangle
            self.board_scores[dim - fourth + x][half - x] = 3
            self.board_scores[dim - fourth + x][half + x] = 3

            # bottom triangle
            self.board_scores[half - x][dim - fourth + x] = 3
            self.board_scores[half + x][dim - fourth + x] = 3

    def place_word(self, word, direction, start):
        '''
        Place a word on the board and returns True if successful
        
        Keyword Arguments:
        word (String) -- the word being placed
        direction (String) -- either "down" or "right"
        start (Tuple of Natural Numbers) -- starting point of the word
        
        Exceptions:
        IndexError
        '''
        try:
            list_of_letters = [char for char in word.upper()]
            if direction == "down":
                for x in range(len(word)):
                    self.board_letters[start[1] + x][start[0]] = list_of_letters[x]
                return True
            elif direction == "right":
                for x in range(len(word)):
                    self.board_letters[start[1]][start[0] + x] = list_of_letters[x]
                return True
        except IndexError as e:
            print(e)
            print("The word you inputted is either too long or the starting point is invalid.")
            return False

    def get_guesses(self):
        '''Return the list of guesses so far'''
        return self.guesses

    def get_scoreboard(self):
        '''Return the NumPy array containing the score weights of the board'''
        return self.board_scores

    def get_letterboard(self):
        '''Return the board with the placed words'''
        return self.board_letters

# WordClass
# class containing functions to do with an entered word
#  - check word validity
#  - get word score
#  - add word score to player

class WordClass:
    '''
    Represent an entered word in the game of scrabble

    Class variables:
    word (String) -- the guessed word
    starting_point (Tuple of Natural Numbers) -- the starting point of the word on the board
    direction (String) -- the direction of the word, either "down" or "right"
    player (PlayerClass) -- the player who entered the word
    used_letters (List of Characters) -- list of letters used by the player to make the word
    '''
    def __init__(self, word, start, direction, player):
        '''
        Constructor
        
        Keyword Arguments:
        word (String) -- the guessed word
        start (Tuple of Natural Numbers) -- the starting point of the word on the board
        direction (String) -- the direction of the word, either "down" or "right"
        player (PlayerClass) -- the player who entered the word
        used_letters (List of Characters) -- list of letters used by the player to make the word
        '''
        self.word = word.upper()
        self.starting_point = start
        self.direction = direction
        self.player = player
        self.used_letters = []

    # check word is in dictionary
    def word_checker(self):
        '''Return True if the word is in the official Scrabble dictionary'''
        with open('PossibleWords.txt', encoding='utf-8') as f:
            dic = {}

            # adds all the words in scrabble from the txt file into a dictionary
            for words in f:
                bank = f.readlines()
                for idx, ele in enumerate(bank):
                    bank[idx] = ele.replace('\n', '')
            for i, j in enumerate(bank):
                dic[j] = i

            # if the word is in the dictionary created above the function returns valid
        if self.word in dic:
            return True
        else:
            return False

    # check word uses the existing letters on the board properly
    def check_if_word_in_hand(self, board):
        '''
        Return True if every letter in the word is either in the player's hand or
        on the board in it's respective position
        
        Keyword Arguments:
        board (BoardClass) -- the board in the game
        
        Exceptions:
        IndexError'''
        letters_in_word = [char for char in self.word]
        letterboard = board.get_letterboard()
        try:
            for x in range(len(letters_in_word)):
                if self.direction == "down":
                    if letterboard[self.starting_point[0] + x][self.starting_point[1]] == letters_in_word[x]:
                        continue
                    elif letterboard[self.starting_point[0] + x][self.starting_point[1]] == 0 and \
                            letters_in_word[x] in self.player.get_letters():
                        self.used_letters.append(letters_in_word[x])
                        continue
                    else:
                        return False
                if self.direction == "right":
                    if letterboard[self.starting_point[0]][self.starting_point[1] + x] == letters_in_word[x]:
                        continue
                    elif letterboard[self.starting_point[0]][self.starting_point[1] + x] == 0 and \
                            letters_in_word[x] in self.player.get_letters():
                        self.used_letters.append(letters_in_word[x])
                        continue
                    else:
                        return False
            return True
        except IndexError:
            return 'IndexError'

    # check word is not a repeated word
    def check_repeat(self, board):
        '''
        Returns False if the entered word is a repeat of an existing guessed word
        
        Keyword Arguments:
        board (BoardClass) -- the board in the game
        '''
        count = 0
        for i in board.guesses:
            if i == self.word.lower():
                count += 1
        if count >= 2:
            return False
        else:
            return True

    # check word is valid
    def valid_word(self, board):
        '''
        Return True only if the word passes all three checks
        
        Keyword Arguments:
        board (BoardClass) -- the board in the game
        '''
        if (WordClass.word_checker(self) and
                WordClass.check_repeat(self, board) and
                WordClass.check_if_word_in_hand(self, board)):
            return True
        else:
            return False

    def valid_first_word(self, board):
        '''
        Return True if the word starts in the middle row or column
        
        Keyword Arguments:
        board (BoardClass) -- the board in the game'''
        if (self.starting_point[0] == (math.ceil(board.board_dimension / 2) - 1) or 
            self.starting_point[1] == (math.ceil(board.board_dimension / 2) - 1)):
            return True
        else:
            return False

    def calculate_points(self, board):
        '''
        Return the number of points the word scores
        
        Keyword Arguments:
        board (BoardClass) -- the board in the game
        
        Exceptions:
        Return 0'''
        list_of_letters = [char for char in self.word.upper()]
        sum = 0
        scoreboard = board.get_scoreboard()
        try:
            if self.direction == "down":
                for x in range(len(self.word)):
                    sum += (scoreboard[self.starting_point[0] + x][self.starting_point[1]] * letter_value.get(
                        list_of_letters[x]))
            else:
                for x in range(len(self.word)):
                    sum += (scoreboard[self.starting_point[0]][self.starting_point[1] + x] * letter_value.get(
                        list_of_letters[x]))

            return sum
        except:
            return 0

    def return_used_letters(self):
        '''Return the list of used letters'''
        return self.used_letters

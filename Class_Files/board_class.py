# class containing functions to do with the board
#  - places word

import numpy as np

global BOARD_DIMENSION
BOARD_DIMENSION = 5

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

board1 = BoardClass()
print(board1.board_letters)
print(board1.board_scores)
board1.place_word("word", "down", (0,0))
print(board1.board_letters)

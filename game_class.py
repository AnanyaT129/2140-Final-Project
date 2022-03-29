from scrabble_module import PlayerClass, BagClass, BoardClass, WordClass

# class containing functions to do with the game
#  - Update round number
#  - Check for game end
#  - Game start
#  - Game end
#  - Game turn

class GameClass:
    def __init__(self):
        self.round_number = 0
        self.skipped_turns = [0,0]
        self.current_board = None
        self.player1 = None
        self.player2 = None
        self.bag = None
    
    def update_round_num(self):
        self.round_number += 1
        return self.round_number

    def check_game_end(self):
        if self.skipped_turns == [2,2]:
            return True
        else:
            return False
    
    def game_start(self, player1, player2):
        self.current_board = BoardClass()
        self.bag = BagClass()
        self.player1 = PlayerClass(player1, self.bag)
        self.player2 = PlayerClass(player2, self.bag)

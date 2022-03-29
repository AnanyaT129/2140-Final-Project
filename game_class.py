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
    
    def game_start(self, player1_name, player2_name):
        self.current_board = BoardClass()
        self.bag = BagClass()
        self.player1 = PlayerClass(player1_name, self.bag)
        self.player2 = PlayerClass(player2_name, self.bag)
    
    # need to add skips
    def game_turn(self, word, start, direction, player):
        entered_word = WordClass(word, start, direction, player)
        if WordClass.valid_word(entered_word) == True:
            points = entered_word.calculate_points
            if points != 0:
                self.current_board.place_word(word, start, direction)
                player.update_score(points)
                used_letters = entered_word.return_used_letters()
                for x in used_letters:
                    player.remove_letter(x)
                player.replenish_letters(self.bag)
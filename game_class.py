from scrabble_classes import PlayerClass, BagClass, BoardClass, WordClass

# class containing functions to do with the game
#  - Check for game end
#  - Game start
#  - Game end
#  - Game turn

class GameClass:
    def __init__(self):
        self.skipped_turns = [0,0]
        self.current_board = None
        self.player1 = None
        self.player2 = None
        self.bag = None

    def check_game_end(self):
        if self.skipped_turns == [2,2] or self.bag.get_bag_size() == 0:
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
        if ((self.current_board.guesses == [] and 
            entered_word.valid_first_word(self.current_board) and 
            entered_word.valid_word(self.current_board)) or
            (self.current_board.guesses != [] and entered_word.valid_word(self.current_board))):
            points = entered_word.calculate_points(self.current_board)
            if points != 0:
                self.current_board.place_word(word, direction, start)
                player.update_score(points)
                used_letters = entered_word.return_used_letters()
                for x in used_letters:
                    player.remove_letter(x)
                player.replenish_letters(self.bag)

def print_array(arr):
    for x in range(len(arr)):
        print(arr[x])

if __name__ == "__main__":
    game = GameClass()
    p1_name = input("Enter player 1 name: ")
    p2_name = input("Enter player 2 name: ")
    game.game_start(p1_name, p2_name)

    while game.check_game_end() == False:
        print_array(game.current_board.board_letters)
        print("Player 1 hand: ", end="")
        print(game.player1.get_letters())
        i_word = input("Enter word to play: ")
        x = int(input("Enter start x: "))
        y = int(input("Enter start y: "))
        start = (x, y)
        direction = input("Enter down or right")
        game.game_turn(i_word, start, direction, game.player1)
        print_array(game.current_board.board_letters)
        print("Player 1 score: ", end="")
        print(game.player1.get_score())
        print("Player 2 hand: ", end="")
        print(game.player2.get_letters())
        i_word = input("Enter word to play: ")
        x = int(input("Enter start x: "))
        y = int(input("Enter start y: "))
        start = (x, y)
        direction = input("Enter down or right")
        game.game_turn(i_word, start, direction, game.player2)
        print_array(game.current_board.board_letters)
        print("Player 2 score: ", end="")
        print(game.player2.get_score())
        print("Scores: ", end="")
        print(game.player1.get_score(), game.player2.get_score())
    print("game end!")
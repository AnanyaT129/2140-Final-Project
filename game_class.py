# Contains the class combining base functions to create game functions

from scrabble_classes import PlayerClass, BagClass, BoardClass, WordClass

# class containing functions to do with the game
#  - Check for game end
#  - Game start
#  - Game end
#  - Game turn

class GameClass:
    '''
    Represent the game of scrabble

    Class variables:
    skipped_turns (List of Natural Numbers) -- Represents the number of skipped turns for each player
    current_board (BoardClass or None) -- The board in the game
    player1 (PlayerClass or None) -- Player 1 in the game
    player2 (PlayerClass or None) -- Player 2 in the game
    bag (BagClass or None) -- the bag of letters in the game
    winner (PlayerClass or None) -- the player who currently has the higher score in the game
    '''
    def __init__(self):
        '''Constructor'''
        self.skipped_turns = [0, 0]
        self.current_board = None
        self.player1 = None
        self.player2 = None
        self.bag = None
        self.winner = None

    def get_p1_name(self):
        '''Return the name of player 1'''
        return self.player1.name

    def get_p2_name(self):
        '''Return the name of player 2'''
        return self.player2.name
    
    def check_game_end(self):
        '''Returns True if either condition to end the game has been met'''
        if self.skipped_turns == [2, 2] or self.bag.get_bag_size() == 0:
            return True
        else:
            return False

    def game_start(self, player1_name, player2_name):
        '''Start the game by initializing the class variables'''
        self.current_board = BoardClass()
        self.bag = BagClass()
        self.player1 = PlayerClass(player1_name, self.bag)
        self.player2 = PlayerClass(player2_name, self.bag)

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

    def update_winner(self):
        '''Update winner to the player with the higher score'''
        if self.player1.get_score() > self.player2.get_score():
            self.winner = self.player1
        elif self.player1.get_score() < self.player2.get_score():
            self.winner = self.player2
        else:
            self.winner = None

    @staticmethod
    def print_array(arr):
        '''Print array row by row'''
        for x in range(len(arr)):
            print(arr[x])

# Code to run game in terminal -- out of date and does not contain skips or forfeits
if __name__ == "__main__":
    game = GameClass()
    p1_name = input("Enter player 1 name: ")
    p2_name = input("Enter player 2 name: ")
    game.game_start(p1_name, p2_name)

    while game.check_game_end() == False:
        GameClass.print_array(game.current_board.board_letters)
        print("Player 1 hand: ", end="")
        print(game.player1.get_letters())
        i_word = input("Enter word to play: ")
        x = int(input("Enter start x: "))
        y = int(input("Enter start y: "))
        start = (x, y)
        direction = input("Enter down or right")
        game.game_turn(i_word, start, direction, game.player1)
        GameClass.print_array(game.current_board.board_letters)
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
        GameClass.print_array(game.current_board.board_letters)
        print("Player 2 score: ", end="")
        print(game.player2.get_score())
        print("Scores: ", end="")
        print(game.player1.get_score(), game.player2.get_score())
    print("game end!")
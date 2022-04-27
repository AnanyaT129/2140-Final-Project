# imports
from tkinter import *
import tkinter as tk
from scrabble_classes import WordClass
from game_class import GameClass

class Errors:
    @staticmethod
    def index_error_message():
        error = Tk()
        error.title('Error Message')
        error.geometry("250x50")
        Label(error, text="The inputted word does not fit on the board.\n"
                          "Try a different starting point and/or direction.").place(x=0, y=0)
        error.mainloop()

    @staticmethod
    def word_error_message():
        worderror = Tk()
        worderror.title('Word Error')
        worderror.geometry("350x90")
        Label(worderror, text="The inputted word either does not exist in the Scrabble dictionary. \n"
                              "The letters in the word are not in your hand. \n"
                              "Or the word has already been used. ").place(x=0, y=0)
        worderror.mainloop()

    @staticmethod
    def skip_error_message():
        error = Tk()
        error.title('Error Message')
        error.geometry("250x50")
        Label(error, text="The player does not have any skips left. \n"
                          "If you cannot play a word, forfeit the game. ").place(x=0, y=0)
        error.mainloop()

    @staticmethod
    def first_word_error_message():
        error = Tk()
        error.title('Error Message')
        error.geometry("250x50")
        Label(error, text="Invalid first word.\n"
                          "Must be placed in the middle row or column. ").place(x=0, y=0)
        error.mainloop()

class GUI:
    def __init__(self):
        # GUI objects
        self.game = GameClass()
        self.player1_textbox = None
        self.player2_textbox = None
        self.direction_str = None
        self.x = None
        self.z = None
        self.letter_matrix = []
        self.matrix = []

        # GUI objects
        self.root = Tk()
        self.instruct = Tk()
        self.window = None
        self.end = None
        self.setup()

    # Helper functions
    def update_player(self):
        if self.x is None:
            self.z = self.game.player1
        elif self.x == 1:
            self.z = self.game.player1
        elif self.x == 2:
            self.z = self.game.player2
    
    def replenish_player_letters(self, g1):
        used_letters = g1.return_used_letters()
        for l in used_letters:
            self.z.remove_letter(l)
        self.z.replenish_letters(self.game.bag)

    def display_error_messages(self, g1):
        if self.game.current_board.get_guesses() == [] and (g1.valid_first_word(self.game.current_board) is False):
            Errors.first_word_error_message()
        
        # Displays appropriate error messages
        elif g1.valid_word(self.game.current_board) is False:
            if g1.check_if_word_in_hand(self.game.current_board) == 'IndexError':
                Errors.index_error_message()
            else:
                Errors.word_error_message()

        else:
            Errors.index_error_message()
    
    def handle_bad_guess(self, g1):
        # Removes guess from list of guesses
        self.game.current_board.guesses.remove(self.game.current_board.guesses[-1])

        # Checks errors to display accurate messages
        self.display_error_messages(g1)
    
    # Main GUI Functions

    def directionfunction(self, direction):
        """Gets the most recent direction inputted by user
        :param direction: str
        """

        if direction == 'up':
            self.direction_str = 'up'
        if direction == 'down':
            self.direction_str = 'down'
        if direction == 'right':
            self.direction_str = 'right'
        if direction == 'left':
            self.direction_str = 'left'

    def startingpoint(self, row, col):
        """Checks if the user input is valid and configures the board if it is
        :param row: int
        :param col: int
        """
        # Updates the current player, z
        self.update_player()

        word = self.game.current_board.guesses[-1].upper()
        g1 = WordClass(self.game.current_board.guesses[-1], (row, col), self.direction_str, self.z)

        # Checks if the word is valid
        if (((len(self.game.current_board.get_guesses()) == 1 and
              g1.valid_first_word(self.game.current_board) and
              g1.valid_word(self.game.current_board)) or
             (len(self.game.current_board.get_guesses()) > 1 and g1.valid_word(self.game.current_board) and
              len(g1.return_used_letters()) < len(word))) and
                self.game.current_board.place_word(word, self.direction_str, (col, row))):

            # If no index error is brought up, the board is changed
            self.update_board(row, col, word)

            # Updates the player's score
            # Checks that the word has a nonzero point value
            points = g1.calculate_points(self.game.current_board)
            self.z.update_score(points)

            # Replenishes player letters
            self.replenish_player_letters(g1)

            # Update the current game winner
            self.game.update_winner()

            # Checks for game end
            if self.game.check_game_end():
                self.end_game()

        else:
            self.handle_bad_guess(g1)

    def forfeit_player1(self):
        """Sets the winner as the other player if one forfeits"""
        self.game.winner = self.game.get_p2_name()
        self.end_game()

    def forfeit_player2(self):
        self.game.winner = self.game.get_p1_name()
        self.end_game()

    def skip(self, player):
        """Skips a turn
        :param player: GameClass
        """
        if player == self.game.player1:
            if self.game.skipped_turns[0] >= 2:
                Errors.skip_error_message()
            else:
                self.game.skipped_turns[0] += 1
        elif player == self.game.player2:
            if self.game.skipped_turns[1] >= 2:
                Errors.skip_error_message()
            else:
                self.game.skipped_turns[1] += 1
        if self.game.skipped_turns[0] >= 2 and self.game.skipped_turns[1] >= 2:
            self.end_game()
    
    # Visuals 

    def initialize_window(self):
        self.window.title('Scrabble')
        self.window.geometry("1000x1000")
    
    def initialize_instructions(self):
        # Instructions
        self.instruct.title('README')
        self.instruct.geometry("260x200")
        Label(self.instruct, text="1) Type in a word and click enter, \n"
                             "2) Select a direction \n"
                             "3) Select a spot on the board to place the word. \n"
                             "4) Must click end turn \n"
                             "\n"
                             "Scores are displayed on the right for both players \n"
                             "The letters on the top represent your hand.").place(x=0, y=0)
        self.instruct.mainloop()

    def setup(self):
        """Beginning window where users enter their usernames"""
        self.root.geometry("250x170")
        T = Text(self.root, height=5, width=52)

        player1_name = Label(self.root, text="player1: ")
        player1_name.place(x=20, y=48)
        player2_name = Label(self.root, text="player2: ")
        player2_name.place(x=20, y=65)
        Instruct = Label(self.root, text="Enter Usernames")
        Instruct.place(x=70, y=25)

        self.player1_textbox = Text(self.root, height=1, width=15)
        self.player1_textbox.pack()
        self.player1_textbox.place(x=65, y=48)

        self.player2_textbox = Text(self.root, height=1, width=15)
        self.player2_textbox.pack()
        self.player2_textbox.place(x=65, y=65)

        enter_names = Button(self.root, text="START", command= self.start_turn, height=1, width=5, bg='white')
        enter_names.place(x=100, y=90)
        T.insert(tk.END, 'Enter the player1 and player2 information and click START')

        self.initialize_instructions()

        self.root.mainloop()
    
    def get_text(self, txtbox):
        """This function receives the words entered into the text box and appends them to a list"""
        result = txtbox.get("1.0", "end")
        self.game.current_board.guesses.append(result)
        for idx, ele in enumerate(self.game.current_board.guesses):
            self.game.current_board.guesses[idx] = ele.replace('\n', '')
        txtbox.delete(1.0, 5.0)
    
    def start_turn(self):
        """Initializes all the graphical components of the game and receives usernames"""
        self.player_1 = self.player1_textbox.get("1.0", "end")
        self.player_2 = self.player2_textbox.get("1.0", "end")
        self.game.game_start(self.player_1, self.player_2)

        self.window = Tk()
        self.initialize_window()

        # Direction buttons
        down = Button(self.window, text="↓", command=lambda: self.directionfunction('down'), height=2, width=4, bg='red')
        down.place(x=70, y=60)
        right = Button(self.window, text="→", command=lambda: self.directionfunction('right'), height=2, width=4, bg='red')
        right.place(x=110, y=60)

        # Position buttons
        for a in range(self.game.current_board.board_dimension):
            self.matrix.append([])
            for b in range(self.game.current_board.board_dimension):
                score = str(self.game.current_board.get_scoreboard()[a][b]) + "x"
                M = Button(self.window, text=score, command=lambda c=a, d=b: self.startingpoint(c, d), height=2, width=4,
                           bg='white')
                M.place(x=(200 + (40 * b)), y=(100 + (43 * a)))
                self.matrix[a].append(M)

        # Hand, score, turn graphics
        player_l1 = Label(self.window, text=self.game.player1.get_letters()[0], height=3, width=6, bg='red')
        player_l1.place(x=320, y=17)
        player_l2 = Label(self.window, text=self.game.player1.get_letters()[1], height=3, width=6, bg='red')
        player_l2.place(x=380, y=17)
        player_l3 = Label(self.window, text=self.game.player1.get_letters()[2], height=3, width=6, bg='red')
        player_l3.place(x=440, y=17)
        player_l4 = Label(self.window, text=self.game.player1.get_letters()[3], height=3, width=6, bg='red')
        player_l4.place(x=500, y=17)
        player_l5 = Label(self.window, text=self.game.player1.get_letters()[4], height=3, width=6, bg='red')
        player_l5.place(x=560, y=17)
        player_l6 = Label(self.window, text=self.game.player1.get_letters()[5], height=3, width=6, bg='red')
        player_l6.place(x=620, y=17)
        player_l7 = Label(self.window, text=self.game.player1.get_letters()[6], height=3, width=6, bg='red')
        player_l7.place(x=680, y=17)
        displays_turn = Label(self.window, text=f"TURN: {self.game.get_p1_name()}", height=2, width=10, bg='red')
        displays_turn.place(x=800, y=17)
        score_label = Label(self.window, text="SCORES:", height=2, width=10, bg='red')
        score_label.place(x=800, y=60)
        player1_points = Label(self.window, text=f"{self.game.get_p1_name()}: {self.game.player1.get_score()}", height=2, width=10, bg='red')
        player1_points.place(x=800, y=100)
        player2_points = Label(self.window, text=f"{self.game.get_p2_name()}: {self.game.player2.get_score()}", height=2, width=10, bg='red')
        player2_points.place(x=800, y=140)

        # Matrix of letters in a player's hand for easy manipulation
        self.letter_matrix = [player_l1, player_l2, player_l3, player_l4, player_l5, player_l6, player_l7, displays_turn,
                         player1_points, player2_points]

        txtbox = Text(self.window, height=1, width=19)
        txtbox.pack()
        txtbox.place(x=10, y=130)

        btnRead = Button(self.window, height=1, width=4, text="Enter", command=lambda: self.get_text(txtbox))
        btnRead.pack()
        btnRead.place(x=70, y=160)

        player1skip = Button(self.window, height=1, width=10, text="Player 1 Skip", command=lambda: self.skip(self.game.player1))
        player1skip.pack()
        player1skip.place(x=10, y=250)

        player2skip = Button(self.window, height=1, width=10, text="Player 2 Skip", command=lambda: self.skip(self.game.player2))
        player2skip.pack()
        player2skip.place(x=90, y=250)

        player1_button = Button(self.window, height=3, width=10, text=f'End turn for \n{self.game.get_p1_name()}', command=self.end_turn_player1)
        player1_button.pack()
        player1_button.place(x=10, y=190)

        player2_button = Button(self.window, height=3, width=10, text=f'End turn for \n{self.game.get_p2_name()}', command=self.end_turn_player2)
        player2_button.pack()
        player2_button.place(x=90, y=190)

        player1_forfeit = Button(self.window, height=3, width=10, text=f'{self.game.get_p1_name()} \nforfeit', command=self.forfeit_player1)
        player1_forfeit.pack()
        player1_forfeit.place(x=10, y=310)

        player2_forfeit = Button(self.window, height=3, width=10, text=f'{self.game.get_p2_name()} \nforfeit', command=self.forfeit_player2)
        player2_forfeit.pack()
        player2_forfeit.place(x=90, y=310)

        self.window.mainloop()

    def update_board(self, row, col, word):
        if self.direction_str == 'right':
            for i in range(row, row + 1):
                for j in range(col, len(word) + col):
                    self.matrix[i][j].config(text=word[j - col], bg='orange')

        if self.direction_str == 'down':
            for i in range(len(word)):
                self.matrix[row + i][col].config(text=word[i], bg='orange')
        
    def end_turn_player1(self):
        """Changes the hand so that it displays the other player's hand, updates score"""
        self.x = 2
        self.letter_matrix[0].config(text=self.game.player2.get_letters()[0])
        self.letter_matrix[1].config(text=self.game.player2.get_letters()[1])
        self.letter_matrix[2].config(text=self.game.player2.get_letters()[2])
        self.letter_matrix[3].config(text=self.game.player2.get_letters()[3])
        self.letter_matrix[4].config(text=self.game.player2.get_letters()[4])
        self.letter_matrix[5].config(text=self.game.player2.get_letters()[5])
        self.letter_matrix[6].config(text=self.game.player2.get_letters()[6])
        self.letter_matrix[7].config(text=f"TURN: {self.game.get_p2_name()}")
        self.letter_matrix[8].config(text=f" {self.game.get_p1_name()}: {self.game.player1.get_score()}")
        self.letter_matrix[9].config(text=f" {self.game.get_p2_name()}: {self.game.player2.get_score()}")

    def end_turn_player2(self):
        self.x = 1
        self.letter_matrix[0].config(text=self.game.player1.get_letters()[0])
        self.letter_matrix[1].config(text=self.game.player1.get_letters()[1])
        self.letter_matrix[2].config(text=self.game.player1.get_letters()[2])
        self.letter_matrix[3].config(text=self.game.player1.get_letters()[3])
        self.letter_matrix[4].config(text=self.game.player1.get_letters()[4])
        self.letter_matrix[5].config(text=self.game.player1.get_letters()[5])
        self.letter_matrix[6].config(text=self.game.player1.get_letters()[6])
        self.letter_matrix[7].config(text=f"TURN: {self.game.get_p1_name()}")
        self.letter_matrix[8].config(text=f" {self.game.get_p1_name()}: {self.game.player1.get_score()}")
        self.letter_matrix[9].config(text=f" {self.game.get_p2_name()}: {self.game.player2.get_score()}")

    def end_game(self):
        """Game ending message"""
        self.end = Tk()
        self.end.title('End Game Screen')
        self.end.geometry("125x100")
        Label(self.end, text=f'The game has ended! \n'
                        f'The winner is {self.game.winner}!!').place(x=0, y=0)
        close = Button(self.end, text="Close", command=self.end_all, height=1, width=4, bg='white')
        close.place(x=40, y=60)
        self.end.mainloop()
    
    def end_all(self):
        """Closes windows when the game is over"""
        self.instruct.destroy()
        self.end.destroy()
        self.window.destroy()
        self.root.destroy()
    
    
overall = GUI()
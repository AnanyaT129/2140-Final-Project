# imports
from tkinter import *
import tkinter as tk
from scrabble_classes import PlayerClass, BagClass, BoardClass, WordClass
from game_class import GameClass

# global variables
game = GameClass()

x = None
z = None


# helper functions
def directionfunction(direction):
    """When the direction button on the interface is clicked, the function tells the starting point function which direction to place the letters
    the backend function must trigger to identify if there is any space for the word.
    """

    global direction_str
    direction_str = 'None'

    if direction == 'up':
        direction_str = 'up'
    if direction == 'down':
        direction_str = 'down'
    if direction == 'right':
        direction_str = 'right'
    if direction == 'left':
        direction_str = 'left'


# Check if the inputted word is valid then according to the starting point and direction, place each letter in the word

def startingpoint(row, col):
    """When a position on the grid is clicked the program places the letters starting from the point and in a direction stated above.
            The backend must determine whether the position is valid according to the length of the word and direction"""

    global x
    global z

    if x is None:
        z = game.player1

    if x == 1:
        z = game.player1

    if x == 2:
        z = game.player2

    word = game.current_board.guesses[-1].upper()
    g1 = WordClass(game.current_board.guesses[-1], (row, col), direction_str, z)

    # if the word is valid
    if (((len(game.current_board.get_guesses()) == 1 and
          g1.valid_first_word(game.current_board) and
          g1.valid_word(game.current_board)) or
         (len(game.current_board.get_guesses()) > 1 and g1.valid_word(game.current_board) and
              len(g1.return_used_letters()) < len(word))) and
            game.current_board.place_word(word, direction_str, (col, row))):

        GameClass.print_array(game.current_board.board_letters)

        # place the word on the board
        if direction_str == 'right':
            for i in range(row, row + 1):
                for j in range(col, len(word) + col):
                    matrix[i][j].config(text=word[j - col], bg='orange')

        if direction_str == 'down':
            for i in range(len(word)):
                matrix[row + i][col].config(text=word[i], bg='orange')

        # place the word on the backend board
        # game.current_board.place_word(word, direction_str, (col, row))

        # update player score
        # check that the word has a nonzero point value
        points = g1.calculate_points(game.current_board)
        z.update_score(points)

        # replenish player letters
        used_letters = g1.return_used_letters()
        for l in used_letters:
            z.remove_letter(l)
        z.replenish_letters(game.bag)

        game.update_winner()

        # check for game end
        if game.check_game_end():
            end_game()

    else:
        # remove guess from list of guesses
        game.current_board.guesses.remove(game.current_board.guesses[-1])
        print(game.current_board.guesses)

        # checks errors to display accurate messages
        if game.current_board.get_guesses() == [] and (g1.valid_first_word(game.current_board) is False):
            first_word_error_message()
        elif g1.valid_word(game.current_board) is False:
            if g1.check_if_word_in_hand(game.current_board) == 'IndexError':
                index_error_message()
            else:
                word_error_message()
        else:
            index_error_message()


def end_turn_player1():
    global x
    x = 2
    print('End turn here for player 1')

    letter_matrix[0].config(text=game.player2.get_letters()[0])
    letter_matrix[1].config(text=game.player2.get_letters()[1])
    letter_matrix[2].config(text=game.player2.get_letters()[2])
    letter_matrix[3].config(text=game.player2.get_letters()[3])
    letter_matrix[4].config(text=game.player2.get_letters()[4])
    letter_matrix[5].config(text=game.player2.get_letters()[5])
    letter_matrix[6].config(text=game.player2.get_letters()[6])
    letter_matrix[7].config(text=f"TURN: {game.get_p2_name()}")
    letter_matrix[8].config(text=f" {game.get_p1_name()}: {game.player1.get_score()}")
    letter_matrix[9].config(text=f" {game.get_p2_name()}: {game.player2.get_score()}")

def end_turn_player2():
    global x
    x = 1
    print('End turn here for player 2')
    letter_matrix[0].config(text=game.player1.get_letters()[0])
    letter_matrix[1].config(text=game.player1.get_letters()[1])
    letter_matrix[2].config(text=game.player1.get_letters()[2])
    letter_matrix[3].config(text=game.player1.get_letters()[3])
    letter_matrix[4].config(text=game.player1.get_letters()[4])
    letter_matrix[5].config(text=game.player1.get_letters()[5])
    letter_matrix[6].config(text=game.player1.get_letters()[6])
    letter_matrix[7].config(text=f"TURN: {game.get_p1_name()}")
    letter_matrix[8].config(text=f" {game.get_p1_name()}: {game.player1.get_score()}")
    letter_matrix[9].config(text=f" {game.get_p2_name()}: {game.player2.get_score()}")

def end_all():
    end.destroy()
    window.destroy()
    root.destroy()

def end_game():
    global end
    end = Tk()
    end.title('End Game Screen')
    end.geometry("250x100")
    Label(end, text=f'The game has ended! \n'
                     'The winner is {game.winner} !!').place(x=0, y=0)
    close = Button(end, text="Close", command=end_all, height=2, width=4, bg='white')
    close.place(x=30, y=40)
    end.mainloop()

def forfeit_player1():
    game.winner = game.player2
    end_game()

def forfeit_player2():
    game.winner = game.player1
    end_game()

def get_text(txtbox):
    """This function receives the words entered into the text box and appends them to a list, backend must check if the word is valid"""
    result = txtbox.get("1.0", "end")
    game.current_board.guesses.append(result)
    for idx, ele in enumerate(game.current_board.guesses):
        game.current_board.guesses[idx] = ele.replace('\n', '')
    print(game.current_board.guesses)
    txtbox.delete(1.0, 5.0)


# creates a board, interactive textbox where user inputs a word, and buttons which determine direction word is placed
# starting point must reference position on list

def index_error_message():
    error = Tk()
    error.title('Error Message')
    error.geometry("250x50")
    Label(error, text="The inputted word does not fit on the board.\n"
                      "Try a different starting point and/or direction.").place(x=0, y=0)
    error.mainloop()


def word_error_message():
    worderror = Tk()
    worderror.title('Word Error')
    worderror.geometry("350x90")
    Label(worderror, text="The inputted word either does not exist in the Scrabble dictionary. \n"
                          "The letters in the word are not in your hand. \n"
                          "Or the word has already been used. ").place(x=0, y=0)
    worderror.mainloop()


def skip_error_message():
    error = Tk()
    error.title('Error Message')
    error.geometry("250x50")
    Label(error, text="The player does not have any skips left. \n"
                      "If you cannot play a word, forfeit the game. ").place(x=0, y=0)
    error.mainloop()


def first_word_error_message():
    error = Tk()
    error.title('Error Message')
    error.geometry("250x50")
    Label(error, text="Invalid first word.\n"
                      "Must be placed in the middle row or column. ").place(x=0, y=0)
    error.mainloop()

def skip(player):
    if player == game.player1:
        if game.skipped_turns[0] >= 2:
            skip_error_message()
        else:
            game.skipped_turns[0] += 1
    elif player == game.player2:
        if game.skipped_turns[1] >= 2:
            skip_error_message()
        else:
            game.skipped_turns[1] += 1
    if game.skipped_turns[0] >= 2 and game.skipped_turns[1] >= 2:
        end_game()


def start_turn():
    player_1 = player1_textbox.get("1.0", "end")
    player_2 = player2_textbox.get("1.0", "end")

    game.game_start(player_1, player_2)
    print(game.current_board.get_guesses())

    global window
    window = Tk()
    window.title('Scrabble')
    window.geometry("1000x1000")

    # Graphical setup of the game

    # Direction buttons
    up = Button(window, text="↑", command=lambda: directionfunction('up'), height=2, width=4, bg='red')
    up.place(x=70, y=17)
    down = Button(window, text="↓", command=lambda: directionfunction('down'), height=2, width=4, bg='red')
    down.place(x=70, y=60)
    right = Button(window, text="→", command=lambda: directionfunction('right'), height=2, width=4, bg='red')
    right.place(x=110, y=60)
    left = Button(window, text="←", command=lambda: directionfunction('left'), height=2, width=4, bg='red')
    left.place(x=30, y=60)

    # Position buttons
    global matrix
    matrix = []

    for a in range(game.current_board.board_dimension):
        matrix.append([])
        for b in range(game.current_board.board_dimension):
            score = str(game.current_board.get_scoreboard()[a][b]) + "x"
            M = Button(window, text=score, command=lambda c=a, d=b: startingpoint(c, d), height=2, width=4, bg='white')
            M.place(x=(200 + (40 * b)), y=(100 + (43 * a)))
            matrix[a].append(M)

    # Hand graphics
    global letter_matrix

    player_l1 = Label(window, text=game.player1.get_letters()[0], height=3, width=6, bg='red')
    player_l1.place(x=320, y=17)

    player_l2 = Label(window, text=game.player1.get_letters()[1], height=3, width=6, bg='red')
    player_l2.place(x=380, y=17)

    player_l3 = Label(window, text=game.player1.get_letters()[2], height=3, width=6, bg='red')
    player_l3.place(x=440, y=17)
    player_l4 = Label(window, text=game.player1.get_letters()[3], height=3, width=6, bg='red')
    player_l4.place(x=500, y=17)
    player_l5 = Label(window, text=game.player1.get_letters()[4], height=3, width=6, bg='red')
    player_l5.place(x=560, y=17)
    player_l6 = Label(window, text=game.player1.get_letters()[5], height=3, width=6, bg='red')
    player_l6.place(x=620, y=17)
    player_l7 = Label(window, text=game.player1.get_letters()[6], height=3, width=6, bg='red')
    player_l7.place(x=680, y=17)
    displays_turn = Label(window, text=f"TURN: {player_1}", height=2, width=10, bg='red')
    displays_turn.place(x=800, y=17)
    score_label = Label(window, text="SCORES:", height=2, width=10, bg='red')
    score_label.place(x=800, y=60)
    player1_points = Label(window, text=f"{player_1}: {game.player1.get_score()}", height=2, width=10, bg='red')
    player1_points.place(x=800, y=100)
    player2_points = Label(window, text=f"{player_2}: {game.player2.get_score()}", height=2, width=10, bg='red')
    player2_points.place(x=800, y=140)

    letter_matrix = [player_l1, player_l2, player_l3, player_l4, player_l5, player_l6, player_l7, displays_turn, player1_points, player2_points]

    # use textbox to enter input word, check if it is valid and then change the appearance of the button so that it shows the letter problem

    txtbox = Text(window, height=1, width=19)
    txtbox.pack()
    txtbox.place(x=10, y=130)

    btnRead = Button(window, height=1, width=4, text="Enter", command=lambda: get_text(txtbox))
    btnRead.pack()
    btnRead.place(x=70, y=160)

    player1skip = Button(window, height=1, width=10, text="Player 1 Skip", command=lambda: skip(game.player1))
    player1skip.pack()
    player1skip.place(x=10, y=250)

    player2skip = Button(window, height=1, width=10, text="Player 2 Skip", command=lambda: skip(game.player2))
    player2skip.pack()
    player2skip.place(x=90, y=250)

    player1_button = Button(window, height=3, width=10, text=f'End turn for \n{player_1}', command=end_turn_player1)
    player1_button.pack()
    player1_button.place(x=10, y=190)

    player2_button = Button(window, height=3, width=10, text=f'End turn for \n{player_2}', command=end_turn_player2)
    player2_button.pack()
    player2_button.place(x=90, y=190)

    player1_forfeit = Button(window, height=3, width=10, text=f'{player_1} \nforfeit', command=forfeit_player1)
    player1_forfeit.pack()
    player1_forfeit.place(x=10, y=310)

    player2_forfeit = Button(window, height=3, width=10, text=f'{player_2} \nforfeit', command=forfeit_player2)
    player2_forfeit.pack()
    player2_forfeit.place(x=90, y=310)

    window.mainloop()


# Beginning window where users enter their usernames
root = Tk()
root.geometry("250x170")
T = Text(root, height=5, width=52)

player1_name = Label(root, text="player1: ").place(x=20, y=48)
player2_name = Label(root, text="player2: ").place(x=20, y=65)
Instruct = Label(root, text="Enter Usernames").place(x=70, y=25)

player1_textbox = Text(root, height=1, width=15)
player1_textbox.pack()
player1_textbox.place(x=65, y=48)

player2_textbox = Text(root, height=1, width=15)
player2_textbox.pack()
player2_textbox.place(x=65, y=65)
player2 = player2_textbox.get("1.0", "end")

enter_names = Button(root, text="START", command=start_turn, height=1, width=5, bg='white').place(x=100, y=90)
T.insert(tk.END, 'Enter the player1 and player2 information and click START')
root.mainloop()
# imports
from tkinter import *
import tkinter as tk
from scrabble_classes import PlayerClass, BagClass, BoardClass, WordClass
from game_class import GameClass

# global variables
game = GameClass()

x = None


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

    if x is None:
        x = game.player1

    if x == 1:
        x = game.player1

    if x == 2:
        x = game.player2

    print(x)

    word = game.current_board.guesses[-1].upper()
    g1 = WordClass(game.current_board.guesses[-1], (row, col), direction_str, x)

    print(x)

    # if the word is valid
    if (((game.current_board.guesses == [] and
          g1.valid_first_word(game.current_board)) or
         (game.current_board.guesses != [] and g1.valid_word(game.current_board))) and
            game.current_board.place_word(word, direction_str, (row, col))):

        # check that the word has a nonzero point value
        points = g1.calculate_points(game.current_board)
        if points != 0:
            # place the word on the board
            if direction_str == 'right':
                for i in range(row, row + 1):
                    for j in range(col, len(word) + col):
                        matrix[i][j].config(text=word[j - col], bg='orange')

            if direction_str == 'down':
                for i in range(row, len(word) + row):
                    for j in range(col, col + 1):
                        matrix[i][j].config(text=word[i - row], bg='orange')

            # place the word on the backend board
            game.current_board.place_word(word, direction_str, (row, col))

            # update player score
            x.update_score(points)

            # replenish player letters
            used_letters = g1.return_used_letters()
            for l in used_letters:
                x.remove_letter(x)
            x.replenish_letters(game.bag)

    # checks errors to display accurate messages
    else:
        game.current_board.guesses.remove(game.current_board.guesses[-1])
        if (game.current_board.guesses == [] and g1.valid_first_word(game.current_board)) is False:
            first_word_error_message()
        elif (game.current_board.guesses != [] and g1.valid_word(game.current_board)) is False:
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


def end_turn_player2():
    global x
    x = 1
    print('End turn here for player 2')


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
        if game.skipped_turns[0] > 2:
            skip_error_message()
        else:
            game.skipped_turns[0] += 1
    elif player == game.player2:
        if game.skipped_turns[1] > 2:
            skip_error_message()
        else:
            game.skipped_turns[1] += 1


def start_turn():
    player_1 = player1_textbox.get("1.0", "end")
    player_2 = player2_textbox.get("1.0", "end")

    game.game_start(player_1, player_2)

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
            M = Button(window, text=score, command=lambda: startingpoint(a, b), height=2, width=4, bg='white')
            M.place(x=(200 + (40 * b)), y=(100 + (43 * a)))
            matrix[a].append(M)

    # Hand graphics

    if x is None or x == game.player1:
        player1_l1 = Label(window, text=game.player1.get_letters()[0], height=3, width=6, bg='red').place(x=320, y=17)
        player1_l2 = Label(window, text=game.player1.get_letters()[1], height=3, width=6, bg='red').place(x=380, y=17)
        player1_l3 = Label(window, text=game.player1.get_letters()[2], height=3, width=6, bg='red').place(x=440, y=17)
        player1_l4 = Label(window, text=game.player1.get_letters()[3], height=3, width=6, bg='red').place(x=500, y=17)
        player1_l5 = Label(window, text=game.player1.get_letters()[4], height=3, width=6, bg='red').place(x=560, y=17)
        player1_l6 = Label(window, text=game.player1.get_letters()[5], height=3, width=6, bg='red').place(x=620, y=17)
        player1_l7 = Label(window, text=game.player1.get_letters()[6], height=3, width=6, bg='red').place(x=680, y=17)

        displays_turn = Label(window, text=f"TURN: {player_1}", height=2, width=10, bg='red').place(x=800, y=17)

        player1_points = Label(window, text=f"{player_1}: {game.player1.get_score()}", height=2, width=10,
                               bg='red').place(x=800, y=60)

    if x == game.player2:
        player2_l1 = Label(window, text=game.player2.get_letters()[0], height=3, width=6, bg='red').place(x=320, y=17)
        player2_l2 = Label(window, text=game.player2.get_letters()[1], height=3, width=6, bg='red').place(x=380, y=17)
        player2_l3 = Label(window, text=game.player2.get_letters()[2], height=3, width=6, bg='red').place(x=440, y=17)
        player2_l4 = Label(window, text=game.player2.get_letters()[3], height=3, width=6, bg='red').place(x=500, y=17)
        player2_l5 = Label(window, text=game.player2.get_letters()[4], height=3, width=6, bg='red').place(x=560, y=17)
        player2_l6 = Label(window, text=game.player2.get_letters()[5], height=3, width=6, bg='red').place(x=620, y=17)
        player2_l7 = Label(window, text=game.player2.get_letters()[6], height=3, width=6, bg='red').place(x=680, y=17)

        displays2_turn = Label(window, text=f"TURN: {player_2}", height=1, width=10, bg='red').place(x=800, y=17)

        player2_points = Label(window, text=f"{player_2}: {game.player2.get_score()}", height=2, width=10,
                               bg='red').place(x=800, y=60)

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
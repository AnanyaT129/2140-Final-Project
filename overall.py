# imports
from tkinter import *
import tkinter as tk
from scrabble_classes import PlayerClass, BagClass, BoardClass, WordClass
from game_class import GameClass

# global variables
global direction_str
direction_str = 'none'
global game
game = GameClass()

# helper functions
def directionfunction(direction):
    """When the direction button on the interface is clicked, the function tells the starting point function which direction to place the letters
    the backend function must trigger to identify if there is any space for the word.
    """
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
    word = game.current_board.guesses[-1].upper()

    g1 = WordClass(game.current_board.guesses[-1], (row, col), direction_str, game.player1)

    if g1.valid_word(game.current_board) is False:
        game.current_board.guesses.remove(game.current_board.guesses[-1])
        worderror = Tk()
        worderror.title('Word Error')
        worderror.geometry("330x90")
        Label(worderror, text="The inputted word either does not exist in the Scrabble dictionary. \n"
                                "The letters in the word are not in your hand. \n"
                                "Or the word has already been used. ").place(x=0, y=0)
        worderror.mainloop()

    else:
        if BoardClass().place_word(word, direction_str, (row, col)) is True:
            if direction_str == 'right':
                for i in range(row, row + 1):
                    for j in range(col, len(word) + col):
                        matrix[i][j].config(text=word[j - col], bg='orange')

            if direction_str == 'down':
                for i in range(row, len(word) + row):
                    for j in range(col, col + 1):
                        matrix[i][j].config(text=word[i - row], bg='orange')

        else:
            game.current_board.guesses.remove(game.current_board.guesses[-1])
            error = Tk()
            error.title('Error Message')
            error.geometry("250x50")
            Label(error, text="The inputted word does not fit on the board.\n"
                                "Try a different starting point and/or direction.").place(x=0, y=0)
            error.mainloop()

def end_turn():
        print('End turn here')

def get_text(txtbox):
    """This function receives the words entered into the text box and appends them to a list, backend must check if the word is valid"""
    result = txtbox.get("1.0", "end")
    print(result)
    game.current_board.guesses.append(result)
    for idx, ele in enumerate(game.current_board.guesses):
        game.current_board.guesses[idx] = ele.replace('\n', '')
    print(game.current_board.guesses)
    txtbox.delete(1.0, 5.0)

# creates a board, interactive textbox where user inputs a word, and buttons which determine direction word is placed
# starting point must reference position on list

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
    M00 = Button(window, text="3x", command=lambda: startingpoint(0, 0), height=2, width=4, bg='white')
    M00.place(x=200, y=100)
    M01 = Button(window, text=" ", command=lambda: startingpoint(0, 1), height=2, width=4, bg='white')
    M01.place(x=240, y=100)
    M02 = Button(window, text="2x", command=lambda: startingpoint(0, 2), height=2, width=4, bg='white')
    M02.place(x=280, y=100)
    M03 = Button(window, text=" ", command=lambda: startingpoint(0, 3), height=2, width=4, bg='white')
    M03.place(x=320, y=100)
    M04 = Button(window, text="3x", command=lambda: startingpoint(0, 4), height=2, width=4, bg='white')
    M04.place(x=360, y=100)
    M10 = Button(window, text=" ", command=lambda: startingpoint(1, 0), height=2, width=4, bg='white')
    M10.place(x=200, y=143)
    M11 = Button(window, text=" ", command=lambda: startingpoint(1, 1), height=2, width=4, bg='white')
    M11.place(x=240, y=143)
    M12 = Button(window, text=" ", command=lambda: startingpoint(1, 2), height=2, width=4, bg='white')
    M12.place(x=280, y=143)
    M13 = Button(window, text=" ", command=lambda: startingpoint(1, 3), height=2, width=4, bg='white')
    M13.place(x=320, y=143)
    M14 = Button(window, text=" ", command=lambda: startingpoint(1, 4), height=2, width=4, bg='white')
    M14.place(x=360, y=143)
    M20 = Button(window, text="3x", command=lambda: startingpoint(2, 0), height=2, width=4, bg='white')
    M20.place(x=200, y=186)
    M21 = Button(window, text=" ", command=lambda: startingpoint(2, 1), height=2, width=4, bg='white')
    M21.place(x=240, y=186)
    M22 = Button(window, text="3x", command=lambda: startingpoint(2, 2), height=2, width=4, bg='white')
    M22.place(x=280, y=186)
    M23 = Button(window, text=" ", command=lambda: startingpoint(2, 3), height=2, width=4, bg='white')
    M23.place(x=320, y=186)
    M24 = Button(window, text="3x", command=lambda: startingpoint(2, 4), height=2, width=4, bg='white')
    M24.place(x=360, y=186)
    M30 = Button(window, text=" ", command=lambda: startingpoint(3, 0), height=2, width=4, bg='white')
    M30.place(x=200, y=229)
    M31 = Button(window, text=" ", command=lambda: startingpoint(3, 1), height=2, width=4, bg='white')
    M31.place(x=240, y=229)
    M32 = Button(window, text=" ", command=lambda: startingpoint(3, 2), height=2, width=4, bg='white')
    M32.place(x=280, y=229)
    M33 = Button(window, text=" ", command=lambda: startingpoint(3, 3), height=2, width=4, bg='white')
    M33.place(x=320, y=229)
    M34 = Button(window, text=" ", command=lambda: startingpoint(3, 4), height=2, width=4, bg='white')
    M34.place(x=360, y=229)
    M40 = Button(window, text="3x", command=lambda: startingpoint(4, 0), height=2, width=4, bg='white')
    M40.place(x=200, y=272)
    M41 = Button(window, text=" ", command=lambda: startingpoint(4, 1), height=2, width=4, bg='white')
    M41.place(x=240, y=272)
    M42 = Button(window, text="2x", command=lambda: startingpoint(4, 2), height=2, width=4, bg='white')
    M42.place(x=280, y=272)
    M43 = Button(window, text=" ", command=lambda: startingpoint(4, 3), height=2, width=4, bg='white')
    M43.place(x=320, y=272)
    M44 = Button(window, text="3x", command=lambda: startingpoint(4, 4), height=2, width=4, bg='white')
    M44.place(x=360, y=272)

    global matrix
    matrix = [[M00, M01, M02, M03, M04], [M10, M11, M12, M13, M14], [M20, M21, M22, M23, M24],
              [M30, M31, M32, M33, M34],
              [M40, M41, M42, M43, M44]]

    # Hand graphics
    player1_l1 = Label(window, text=game.player1.get_letters()[0], height=3, width=6, bg='red').place(x=320, y=660)
    player1_l2 = Label(window, text=game.player1.get_letters()[1], height=3, width=6, bg='red').place(x=380, y=660)
    player1_l3 = Label(window, text=game.player1.get_letters()[2], height=3, width=6, bg='red').place(x=440, y=660)
    player1_l4 = Label(window, text=game.player1.get_letters()[3], height=3, width=6, bg='red').place(x=500, y=660)
    player1_l5 = Label(window, text=game.player1.get_letters()[4], height=3, width=6, bg='red').place(x=560, y=660)
    player1_l6 = Label(window, text=game.player1.get_letters()[5], height=3, width=6, bg='red').place(x=620, y=660)
    player1_l7 = Label(window, text=game.player1.get_letters()[6], height=3, width=6, bg='red').place(x=680, y=660)

    # player2_l1 = Label(window, text= 'W', height=3, width=6, bg= 'red').place(x=320, y=660)
    # player2_l2 = Label(window, text= 'W', height=3, width=6, bg= 'red').place(x=380, y=660)
    # player2_l3 = Label(window, text= 'W', height=3, width=6, bg= 'red').place(x=440, y=660)
    # player2_l4 = Label(window, text= 'W', height=3, width=6, bg= 'red').place(x=500, y=660)
    # player2_l5 = Label(window, text= 'W', height=3, width=6, bg= 'red').place(x=560, y=660)
    # player2_l6 = Label(window, text= 'W', height=3, width=6, bg= 'red').place(x=620, y=660)
    # player2_l7 = Label(window, text= 'W', height=3, width=6, bg= 'red').place(x=680, y=660)

    # use textbox to enter input word, check if it is valid and then change the appearance of the button so that it shows the letter problem

    txtbox = Text(window, height=1, width=19)
    txtbox.pack()
    txtbox.place(x=10, y=130)

    btnRead = Button(window, height=1, width=4, text="Enter", command=get_text(txtbox))
    btnRead.pack()
    btnRead.place(x=70, y=160)

    endturn = Button(window, height=1, width=8, text="End Turn", command=end_turn)
    endturn.pack()
    endturn.place(x=70, y=190)

    window.mainloop()

#Beginning window where users enter their usernames
root = Tk()
root.geometry("250x170")
T = Text(root, height = 5, width = 52)

player1_name = Label(root, text = "player1: ").place(x = 20, y = 48)
player2_name = Label(root, text = "player2: ").place(x = 20, y = 65)
Instruct = Label(root, text = "Enter Usernames").place(x = 70, y = 25)

player1_textbox = Text(root, height=1, width=15)
player1_textbox.pack()
player1_textbox.place(x=65, y=48)

player2_textbox = Text(root, height=1, width=15)
player2_textbox.pack()
player2_textbox.place(x=65, y=65)
player2 = player2_textbox.get("1.0", "end")

enter_names = Button(root, text="START", command= start_turn, height= 1, width = 5, bg='white').place(x = 100, y = 90)
T.insert(tk.END, 'Enter the player1 and player2 information and click START')
root.mainloop()
# SCRABBLE
**Ananya Tadigadapa and Ben Yoon  
2022 Final Project for EECE2140 at Northeastern University**

## About
This project aimed to create an interactive game of scrabble using Python. The final product was a two person game which can be played through the developed GUI or in terminal.   

Scrabble is a board game in which players randomly pick 7 letters from a bag of 100 as their "hand." In turns, they place new words on a 15x15 board by utilizing the existing letters. They gain points depending on which letters they used and which spots on the board their letters covered.

## Rules
1. The player who places the first word on their board must place it either on the starting x or y axis. 
2. Words must be placed going either down or right. 
3. With the exception of the first word, all words placed must use at least 1 letter of an existing word on the board
4. Words cannot repeat
5. If the word is valid, then points will be calculated as following:
   1. Every letter has a point value associated with it: 
      - 1 - A, E, I, L, N, O, R, S, T, U
      - 2 - D, G
      - 3 - B, C, M, P
      - 4 - F, H, V, W, Y
      - 5 - K
      - 8 - J, X
      - 10 - Q, Z
   2. Some squares will multiply the letter score by 3 and some by 2
   3. Players will recieve points for letters that are part of their word that were already on the board
   4. The points they recieve per turn are the sum of the total points for each letter in the word
6. Players also have the option to either skip their turn, with a maximum of 2 skips each per game, or forfeit the game
7. The game ends when either the bag is empty, both players have skipped their turn twice, or one player forfeits
   - The winner is the player with more points or 
   - The player who didn't forfeit

## How to play - GUI
To play with the GUI, run the file ```overall.py```.  

1. Enter each players names when prompted, then press ```start```.
2. Each turn must follow the rules above. 
3. The board squares without a letter are labeled for how much they multiply the score of the letter placed on them (either 3x, 2x, or 1x)
4. The current player's hand is shown above the board, the scores to the right, and the spaces to enter a word on the left
5. When entering a word, first type the whole word out (including existing letters on the board that the word is using) into the text box and press enter.
6. Above the textbox, click the direction that the word will go (down arrow or right arrow)
7. Press the square on the board that the word starts at - meaning the square the first letter of the board is on
   - If the word is valid, it will appear on the board in orange letters
   - If it is not valid, an error message will pop up with the specific issue of that word. Close the message and retry entering a word. 
9. If you want to skip your turn, press the ```skip turn``` button with your username on it
10. If you want to forfeit the game, press the ```forfeit``` button with your username on it
11. Once your turn is over, press the ```End turn``` button with your username on it. The letters on the top will automatically update for the other player, as will the scores. 
12. Once the game ends, a new window will pop up displaying the winner. Press the close button on that window to close all running files for the game. 

## How to play - Terminal
To play in terminal, run the file ``game_class.py```.

1. Enter the players names when prompted
2. Each turn must follow the rules above
3. The current board and current player's hand will be printed before each turn, showing where words are placed
4. When prompted, enter a word by typing the whole word out (including existing letters on the board that the word is using) and pressing enter
5. Then give the row number and column number of the starting point of the word - meaning the square the first letter of the board is on, as prompted
   - Numbers are indexed from 0, so leftmost row and topmost column is 0, the rightmost row and bottommost column is 14, and the middle row and column is 7. 
6. Then input the directon the word is going in
   - Directions must be a string, either ```"down"``` or ```"right"```
   - No other string will be accepted
7. If the word is valid, then points will be calculated and shown, and the board/current players hand will be displayed for the next player.
8. When the game ends, the winner will be printed and the program will stop running. 

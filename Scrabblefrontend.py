# creates a board, interactive textbox where user inputs a word, and buttons which determine direction word is placed
# starting point must reference position on list

from tkinter import *


window = Tk()
window.title('Scrabble')
window.geometry("1000x1000")

usedwordslst = []


def directionfunction(direction):
   """When the direction button on the interface is clicked, the backend function must trigger to identify if there is any space
   for the word
   """
   if direction == 'up':
      print('Executes up direction')
   if direction == 'down':
      print('Executes down direction')
   if direction == 'right':
      print('Executes right direction')
   if direction == 'left':
      print('Executes left direction')


def startingpoint(row, col):
   """When a position on the grid is clicked the program outputs the coordinates of the position clicked. The backend must determine whether the position
   is valid according to the length of the word and direction"""
   print(row, col)
   if (0,0):
      M00.config(text = 'A', bg = 'orange')

def get_text():
   """This function receives the words entered into the text box and appends them to a list, backend must check if the word is valid"""
   result = txtbox.get("1.0", "end")
   usedwordslst.append(result)
   for idx, ele in enumerate(usedwordslst):
      usedwordslst[idx] = ele.replace('\n', '')
   print(usedwordslst)
   txtbox.delete(1.0,5.0)


#Graphical setup of the game
up = Button(window, text="↑", command= lambda: directionfunction('up'), height= 2, width = 4, bg='red')
up.place(x=70, y=17)
down = Button(window, text="↓", command= lambda: directionfunction('down'), height= 2, width = 4, bg='red')
down.place(x=70, y=60)
right = Button(window, text="→", command= lambda: directionfunction('right'), height= 2, width = 4, bg='red')
right.place(x=110, y=60)
left = Button(window, text="←", command= lambda: directionfunction('left'), height= 2, width = 4, bg='red')
left.place(x=30, y=60)

M00 = Button(window, text="3x", command=lambda:startingpoint(0,0), height= 2, width = 4, bg='white')
M00.place(x=200, y=100)
M01 = Button(window, text=" ", command=lambda:startingpoint(0,1), height= 2, width = 4, bg='white')
M01.place(x=240, y=100)
M02 = Button(window, text="2x", command=lambda:startingpoint(0,2), height= 2, width = 4, bg='white')
M02.place(x=280, y=100)
M03 = Button(window, text=" ", command=lambda:startingpoint(0,3), height= 2, width = 4, bg='white')
M03.place(x=320, y=100)
M04 = Button(window, text="3x", command=lambda:startingpoint(0,4), height= 2, width = 4, bg='white')
M04.place(x=360, y=100)
M10 = Button(window, text=" ", command=lambda:startingpoint(1,0), height= 2, width = 4, bg='white')
M10.place(x=200, y=143)
M11 = Button(window, text=" ", command=lambda:startingpoint(1,1), height= 2, width = 4, bg='white')
M11.place(x=240, y=143)
M12 = Button(window, text=" ", command=lambda:startingpoint(1,2), height= 2, width = 4, bg='white')
M12.place(x=280, y=143)
M13 = Button(window, text=" ", command=lambda:startingpoint(1,3), height= 2, width = 4, bg='white')
M13.place(x=320, y=143)
M14 = Button(window, text=" ", command=lambda:startingpoint(1,4), height= 2, width = 4, bg='white')
M14.place(x=360, y=143)
M20 = Button(window, text="3x", command=lambda:startingpoint(2,0), height= 2, width = 4, bg='white')
M20.place(x=200, y=186)
M21 = Button(window, text=" ", command=lambda:startingpoint(2,1), height= 2, width = 4, bg='white')
M21.place(x=240, y=186)
M22 = Button(window, text="3x", command=lambda:startingpoint(2,2), height= 2, width = 4, bg='white')
M22.place(x=280, y=186)
M23 = Button(window, text=" ", command=lambda:startingpoint(2,3), height= 2, width = 4, bg='white')
M23.place(x=320, y=186)
M24 = Button(window, text="3x", command=lambda:startingpoint(2,4), height= 2, width = 4, bg='white')
M24.place(x=360, y=186)
M30 = Button(window, text=" ", command=lambda:startingpoint(3,0), height= 2, width = 4, bg='white')
M30.place(x=200, y=229)
M31 = Button(window, text=" ", command=lambda:startingpoint(3,1), height= 2, width = 4, bg='white')
M31.place(x=240, y=229)
M32 = Button(window, text=" ", command=lambda:startingpoint(3,2), height= 2, width = 4, bg='white')
M32.place(x=280, y=229)
M33 = Button(window, text=" ", command=lambda:startingpoint(3,3), height= 2, width = 4, bg='white')
M33.place(x=320, y=229)
M34 = Button(window, text=" ", command=lambda:startingpoint(3,4), height= 2, width = 4, bg='white')
M34.place(x=360, y=229)
M40 = Button(window, text="3x", command=lambda:startingpoint(4,0), height= 2, width = 4, bg='white')
M40.place(x=200, y=272)
M41 = Button(window, text=" ", command=lambda:startingpoint(4,1), height= 2, width = 4, bg='white')
M41.place(x=240, y=272)
M42 = Button(window, text="2x", command=lambda:startingpoint(4,2), height= 2, width = 4, bg='white')
M42.place(x=280, y=272)
M43 = Button(window, text=" ", command=lambda:startingpoint(4,3), height= 2, width = 4, bg='white')
M43.place(x=320, y=272)
M44 = Button(window, text="3x", command=lambda:startingpoint(4,4), height= 2, width = 4, bg='white')
M44.place(x=360, y=272)


#use textbox to enter input word, check if it is valid and then change the appearance of the button so that it shows the letter problem

txtbox = Text(window, height=1, width=19)
txtbox.pack()
txtbox.place(x=10, y=130)

btnRead=Button(window, height=1, width=4, text="Enter", command=get_text)
btnRead.pack()
btnRead.place(x=70, y=160)



#Check if the inputted word is valid then according to the starting point and direction, place each letter in the word


window.mainloop()

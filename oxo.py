from tkinter
 import Tk, PhotoImage, Button, messagebox
window = Tk()
window.title("OXO Game")
window.geometry("300x300")
window.mainloop()
available_space = PhotoImage(file="myButton.png")
player1_taken = PhotoImage(file="myButtonP1.png")
player2_taken = PhotoImage(file="myButtonP2.png")
winner = PhotoImage(file="winner.png")
from tkinter import Tk, PhotoImage
# create a list of squares, assign each element the value None
# [None, None, None, None, None, None, None, None, None]
square = [None]*9
def create_buttons():
square[0] = Button(window, image=available_space, width="100",
, height="100", command= lambda: handle_button_click(0))
from tkinter import Tk, PhotoImage, Button
square[0].place(x=0, y=0)
create_buttons()
print("Button ", button_number, "was clicked")
square[button_number].configure(image=player1_taken,
, command=square_taken)
def square_taken():
messagebox.showinfo("Square Taken", "Square already taken choose
, another!")
counter = 0
global counter
if counter % 2 == 0:
else:
    square[button_number].configure(image=player2_taken,
    command=square_taken)
counter += 1
oxo = [
[' ', ' ', ' '],
[' ', ' ', ' '],
[' ', ' ', ' ']
]
def update_move(square_number, player_number):
square_to_oxo_map = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2],
, [2, 0], [2, 1], [2, 2]]
m = square_to_oxo_map
p = player_number
s = square_number
oxo [m[s][0]][m[s][1]] = p
oxo[square_to_oxo_map[square_number][0]]
, [square_to_oxo_map[square_number][1]] = player_number
check_win()
update_move(button_number, 1)
update_move(button_number, 2)
def check_win():
won = []
won.append(oxo[0][0] == oxo[1][1] == oxo[2][2] and oxo[0][0] != ' ')
won.append(oxo[0][2] == oxo[1][1] == oxo[2][0] and oxo[0][2] != ' ')
for row in range(3):
won.append(oxo[row][0] == oxo[row][1] == oxo[row][2] and oxo[row][0]
, != ' ')
for col in range(3):
won.append(oxo[0][col] == oxo[1][col] == oxo[2][col] and oxo[0][col]
, != ' ')
for i in range(3):
won.append(oxo[i][0] == oxo[i][1] == oxo[i][2] and oxo[i][0] != '
, ')
won.append(oxo[0][i] == oxo[1][i] == oxo[2][i] and oxo[0][i] != '
, ')
if True in won:
    button = Button(window, image=winner, width="300", height="100")
button.pack()







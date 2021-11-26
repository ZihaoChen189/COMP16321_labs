from tkinter import Tk, Canvas
import random

def placefood():
    global food,foodx,foody
    food = canvas.create_rectangle(0,0,snakesize,snakesize,fill='steel blue')
    foodx= random.randint(0,width-snakesize)
    foody= random.randint(0,heigh-snakesize)
    canvas.move(food,foodx,foody)

def Leftkey(event):
    global direction
    direction = 'left'
def Rightkey(event):
    global direction
    direction = 'right'
def Upkey(event):
    global direction
    direction = 'up'
def Downkey(event):
    global direction
    direction = 'down'
def setwindow(w,h):
    window = Tk()
    window.title('snake game')
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2)-(w/2)
    y = (hs/2)-(h/2)
    window.geometry('%dx%d+%d+%d' % (w,h,x,y))
    return window

width = 550
height = 550
window = setwindow(width, height)
canvas = Canvas(window, bg="black",width=width,height=height)
snake = []
snakesize = 15
snake.append(canvas.create_rectangle(snakesize,snakesize,snakesize*2,snakesize*2,fill="white"))
score = 0
txt = 'score:'+str(score)
scoreText = canvas.create_text(width/2, 10, fill='white', font='Times 20 italic bold', text=txt)


canvas.bind('<Left>', Leftkey)
canvas.bind('<Right>', Rightkey)
canvas.bind('<Up>', Upkey)
canvas.bind('<Down>', Downkey)
canvas.focus_set()
direction = 'right'

def overlapping(a,b):
    if a[0] < b[2] and a[2] > b[0] and a[1] < b [3] and a[3] > b[1]:
        return True
    return False

def movesnake():
    canvas.pack()
    position = []
    position.append(canvas.coords(snake[0]))
    if position[0][0] < 0:
        canvas.coords(snake[0],width,position[0][1],width-snakesize,position[0][3])
    elif position[0][2] > width:
        canvas.coords(snake[0],0-snakesize,position[0][1],0,position[0][3])
    elif position[0][3] > height:
        canvas.coords(snake[0],position[0][0],0-snakesize,position[0][2],0)
    elif position[0][1] < 0:
        canvas.coords(snake[0],position[0][0],heigh,position[0][2],heigh-snakesize)
    position.clear()
    position.append(canvas.coords(snake[0]))

    if direction == "left":
        canvas.move(snake[0],-snakesize,0)
    elif direction == "right":
        canvas.move(snake[0],snakesize,0)
    elif direction == "up":
        canvas.move(snake[0],0,-snakesize)
    elif direction == "down":
        canvas.move(snake[0],0,snakesize)
    window.after(90, movesnake)

movesnake()
placefood()
window.mainloop()



import turtle
import random
from turtle import *

fer = turtle.Turtle()
fer.speed(0)
fer.width(5)

colors = ['red', 'green', 'blue', 'purple', 'pink']

def up():
    fer.setheading(90)
    fer.forward(100)
def down():
    fer.setheading(270)
    fer.forward(100)
def left():
    fer.setheading(180)
    fer.forward(100)
def right():
    fer.setheading(0)
    fer.forward(100)
def clickleft(x,y):
    fer.color(random.choice(colors))

def clickright(x,y):
    fer.stamp()

turtle.listen()

turtle.onscreenclick(clickleft, 1)
turtle.onscreenclick(clickright, 3)


turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

turtle.mainloop()
import turtle
import random
from turtle import *

abang = turtle.Turtle()
abang.shape('turtle')
abang.speed(10)
colors = ['red', 'blue','purple','black','green','silver','pink','forestgreen',]


#set color for turtle
abang.color('blue','purple')

#pen width
abang.width(5)

#fill the shape color
abang.begin_fill()
abang.circle(50)
abang.end_fill()

abang.penup()
abang.forward(150)
abang.pendown()

abang.color('red','black')

abang.begin_fill()
for a in range(1):
    abang.circle(80)
abang.end_fill()

for z in range(100):
    randcolor = random.randrange(0, len(colors))
    abang.color(colors[randcolor],colors[random.randrange (0, len(colors))])
    rand1 = random.randrange(-300, 300)
    rand2 = random.randrange(-300, 300)
    abang.penup()
    abang.setpos((rand1, rand2))
    abang.pendown()
    abang.begin_fill()
    abang.circle(random. randrange(0, 80))
    abang.end_fill()

turtle.done()
import turtle
from turtle import Turtle,Screen

screen = Screen()
screen.bgcolor("green")
f = Turtle("turtle")
f.turtlesize(3)
f.width(20)
f.speed(-5)

#inti terpentingnya
def dragging(x, y):
    f.ondrag(None)
    f.setheading(f.towards(x, y))
    f.goto(x,y)
    f.ondrag(dragging)

#menghapus tulisanya
def clickRight(x, y):
    f.clear()

#memulai program
def main():
    turtle.listen()
    f.ondrag(dragging)
    turtle.onscreenclick(clickRight, 3)
    screen.mainloop()
main()
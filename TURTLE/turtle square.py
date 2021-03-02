import turtle

turtle.bgcolor('black')
turtle.speed(15)

for x in range(5):
    for colours in ["magenta", "blue", "red", "cyan", "green", "white", "yellow", "pink", "purple"]:
        turtle.color(colours)
        turtle.pensize(2)
        turtle.left(12)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)

turtle.done()



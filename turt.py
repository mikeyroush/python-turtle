import turtle
from random import choice, randrange


def drawShapes(shapes):
    for j in range(shapes):
        sides = randrange(1, 15)
        for i in range(sides):
            tim.forward(50)
            tim.left(360/sides)
        tim.color(choice(colors))
        tim.left(360/shapes)


def up():
    tim.setheading(90)
    tim.forward(15)


def down():
    tim.setheading(270)
    tim.forward(15)


def left():
    tim.setheading(180)
    tim.forward(15)


def right():
    tim.setheading(0)
    tim.forward(15)


TK_SILENCE_DEPRECATION = 1
tim = turtle.Turtle()
colors = "maroon blue red gray brown tan pink orange yellow"
colors = colors.split()
tim.shape('turtle')
tim.color('green')
tim.speed(5000)

# drawShapes(100)
turtle.listen()

turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

turtle.done()

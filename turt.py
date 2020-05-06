import turtle
import math
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


def race(turtleNum):
    turtleNum = min(turtleNum, len(colors))
    turtles = []
    start = turtle.window_width()/-4
    dx = turtle.window_width()/2/(turtleNum-1)

    for i in range(turtleNum):
        turt = turtle.Turtle()
        color = choice(colors)
        colors.remove(color)
        turt.shape('turtle')
        turt.color(color)
        turt.penup()
        turt.setheading(90)
        turt.setpos((start + i * dx, start))
        turt.pendown()
        turtles.append(turt)

    speeds = [randrange(10, 15) for _ in range(turtleNum)]

    for _ in range(math.floor(turtle.window_height()/2/max(speeds))):
        for index, turt in enumerate(turtles):
            turt.forward(speeds[index])


TK_SILENCE_DEPRECATION = 1
colors = "maroon blue red gray brown tan pink orange green"
colors = colors.split()
# tim = turtle.Turtle()
# tim.shape('turtle')
# tim.color('green')
# tim.speed(5000)

# drawShapes(100)

# turtle.listen()
# turtle.onkey(up, 'Up')
# turtle.onkey(down, 'Down')
# turtle.onkey(left, 'Left')
# turtle.onkey(right, 'Right')

race(5)

turtle.done()

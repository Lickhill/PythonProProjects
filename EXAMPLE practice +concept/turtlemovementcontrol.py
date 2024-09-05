from turtle import Turtle, Screen
import random

arrow = Turtle()
arrow.shape("arrow")
myscreen = Screen()
myscreen.colormode(255)


def changecolor():  # to generate all 16M colors
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    return (
        r,
        g,
        b,
    )


arrow.color(changecolor())
arrow.pensize(7)


def up():
    arrow.setheading(90)


def forward():
    arrow.fd(100)


def down():
    arrow.setheading(270)


def left():
    arrow.setheading(180)


def right():
    arrow.setheading(0)


def clear():
    arrow.reset()
    arrow.color(changecolor())
    arrow.goto(0, 0)


def northwest():
    arrow.setheading(135)


def northeast():
    arrow.setheading(45)


def southeast():
    arrow.setheading(315)


def southwest():
    arrow.setheading(225)


myscreen.listen()
# myscreen.onkey(key="up", fun=arrow.setheading(90))
# myscreen.onkey(key="down", fun=arrow.right(270))
myscreen.onkey(key="w", fun=up)
myscreen.onkey(key="s", fun=down)
myscreen.onkey(key="space", fun=forward)
myscreen.onkey(key="d", fun=right)
myscreen.onkey(key="a", fun=left)
myscreen.onkey(key="c", fun=clear)
myscreen.onkey(key="q", fun=northwest)
myscreen.onkey(key="e", fun=northeast)
myscreen.onkey(key="z", fun=southwest)
myscreen.onkey(key="x", fun=southeast)

myscreen.mainloop()

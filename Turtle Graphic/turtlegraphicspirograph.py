from turtle import Turtle, Screen
import random

arrow = Turtle()
arrow.shape("arrow")
arrow.speed(0)
arrow.pensize(4)

screen = Screen()
screen.colormode(255)


def changecolor():
    r = random.randint(0, 256)
    b = random.randint(0, 256)
    g = random.randint(0, 256)
    return (r, g, b)


for i in range(72):
    arrow.color(changecolor())
    arrow.circle(100)
    arrow.right(5)


screen.mainloop()

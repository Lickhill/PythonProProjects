import random
from turtle import Turtle, Screen

arrow = Turtle()
arrow.shape("arrow")
arrow.pensize(5)
arrow.speed(0)
movements = [90, 180, 0, 270]

# colors = [
#     "white",
#     "black",
#     "gray",
#     "red",
#     "green",
#     "blue",
#     "cyan",
#     "magenta",
#     "yellow",
#     "orange",
#     "purple",
#     "brown",
# ]

screen = Screen()
screen.colormode(255)


def changecolor():  # to generate all 16M colors
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    return (
        r,
        g,
        b,
    )  # this (red, blue, green ) or (x,y,z) is called tupple. tupple is like list but in tupple data cannot be modified unlike list or array


j = 5
for i in range(200):
    # arrow.color(random.choice(colors))
    arrow.color(changecolor())
    arrow.left(random.choice(movements))
    arrow.fd(15)
    j += 0.1
    arrow.pensize(j)


screen.exitonclick()
screen.mainloop()

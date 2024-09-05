from turtle import Turtle, Screen


arrow = Turtle()
arrow.shape("arrow")


angles = [
    60,  # Triangle
    90,  # Square
    108,  # Pentagon
    120,  # Hexagon
    128.57,  # Heptagon
    135,  # Octagon
    140,  # Nonagon
    144,  # Decagon
]

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink"]

j = 0
while j < 8:
    arrow.color(colors[j])
    for i in range(j + 3):
        arrow.fd(100)
        # arrow.right(180 - angles[j])
        arrow.right(360 / (j + 3))
    j += 1


screen = Screen()
screen.exitonclick()

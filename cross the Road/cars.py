from turtle import Turtle
import random


class Cars:
    def __init__(self):
        self.colors = [
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "purple",
            "pink",
            "cyan",
            "magenta",
            "brown",
            "black",
            "gray",
            "lightgray",
            "darkgray",
            "navy",
            "maroon",
            "olive",
            "teal",
            "lime",
        ]
        self.gadi = []
        self.carmovedist = 5

    def spawnthecars(self):
        if random.randint(1, 6) == 1:
            newcar = Turtle("square")
            newcar.shapesize(stretch_len=2, stretch_wid=1)
            newcar.penup()
            newcar.color(random.choice(self.colors))
            newcar.goto(random.randint(200, 250), random.randint(-190, 250))
            self.gadi.append(newcar)

    def movecar(self):
        for car in self.gadi:
            car.bk(self.carmovedist)

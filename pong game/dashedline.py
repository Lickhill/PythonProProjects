from turtle import Turtle


class Dash(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(7)
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(0, -300)
        self.pendown()
        self.setheading(90)
        self.draw()

    def draw(self):
        for i in range(12):
            self.pendown()
            self.fd(40)
            self.penup()
            self.fd(10)

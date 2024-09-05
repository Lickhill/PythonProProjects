from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.speed(0)
        self.color("black")
        self.penup()
        self.goto(0, -220)
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.setheading(90)

    def forward(self):
        self.fd(25)

    def backward(self):
        self.bk(25)

    def left(self):
        self.goto(self.xcor() - 25, self.ycor())

    def right(self):
        self.goto(self.xcor() + 25, self.ycor())

    def reset(self):
        self.goto(0, -220)

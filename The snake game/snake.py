# for i in range(200):
#     screen.update()
#     for turtle in squares:
#         turtle.fd(20)
#         time.sleep(0.001)

from turtle import Turtle


class Snake:
    def __init__(self, screen):
        self.squares = []
        self.screen = screen
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for i in range(3):
            square = Turtle()
            square.penup()
            square.shape("square")
            square.color("white")
            square.speed(0)
            square.goto(-20 * i, 0)  # because the default size of turtle is 20x20
            self.squares.append(square)

    def extend(self):
        square = Turtle()
        square.penup()
        square.shape("square")
        square.color("white")
        square.speed(0)
        self.squares.append(square)

    def forward(self):
        i = len(self.squares) - 2
        while True:
            while i >= 0:
                x = self.squares[i].xcor()
                y = self.squares[i].ycor()
                self.squares[i + 1].goto(x, y)
                i -= 1
            self.squares[0].fd(20)
            i = 1

            if self.squares[0].xcor() > 290:
                self.squares[0].goto(-290, self.squares[0].ycor())
            # if self.squares[0].ycor() > 290:
            #     self.squares[0].goto(self.squares[0].xcor(), -290)
            if self.squares[0].xcor() < -290:
                self.squares[0].goto(290, self.squares[0].ycor())
            # if self.squares[0].ycor() < -290:
            #     self.squares[0].goto(self.squares[0].xcor(), 290)
            break

    def up(self):
        if self.squares[0].heading() != 270:
            self.squares[0].setheading(90)
            self.forward()

    def left(self):
        if self.squares[0].heading() != 0:
            self.squares[0].setheading(180)
            self.forward()

    def right(self):
        if self.squares[0].heading() != 180:
            self.squares[0].setheading(0)
            self.forward()

    def down(self):
        if self.squares[0].heading() != 90:
            self.squares[0].setheading(270)
            self.forward()

    # def function(self):
    #     self.screen.listen()
    #     self.screen.onkey(self.up, "w")
    #     self.screen.onkey(self.left, "a")
    #     self.screen.onkey(self.right, "d")
    #     self.screen.onkey(self.up, "w")
    #     self.screen.onkey(self.down, "s")

    #     self.forward()

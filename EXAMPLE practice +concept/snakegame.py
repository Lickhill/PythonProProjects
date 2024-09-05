from turtle import Turtle, Screen

# import time

screen = Screen()
screen.title("My Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)

squares = []
for i in range(3):
    square = Turtle()
    square.penup()
    square.shape("square")
    square.color("white")
    square.speed(0)
    square.goto(-20 * i, 0)  # because the default size of turtle is 20x20
    squares.append(square)


# for i in range(200):
#     screen.update()
#     for turtle in squares:
#         turtle.fd(20)
#         time.sleep(0.001)


def forward():
    i = len(squares) - 2
    while True:
        while i >= 0:
            x = squares[i].xcor()
            y = squares[i].ycor()
            squares[i + 1].goto(x, y)
            i -= 1
        squares[0].fd(20)
        i = 1

        if (
            squares[0].xcor() > 270
            or squares[0].ycor() > 270
            or squares[0].xcor() < -270
            or squares[0].ycor() < -270
        ):
            screen.exitonclick()
            break


def up():
    squares[0].setheading(90)
    forward()


def left():
    squares[0].setheading(180)
    forward()


def right():
    squares[0].setheading(0)
    forward()


def down():
    squares[0].setheading(270)
    forward()


def function():
    screen.listen()
    screen.onkey(up, "w")
    screen.onkey(left, "a")
    screen.onkey(right, "d")
    screen.onkey(up, "w")
    screen.onkey(down, "s")

    forward()
    screen.mainloop()


function()

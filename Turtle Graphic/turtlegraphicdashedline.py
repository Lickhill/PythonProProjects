from turtle import Turtle, Screen


arrow = Turtle()
arrow.shape("arrow")
arrow.color("black")
i = 0

while i < 6:
    arrow.pendown()
    arrow.fd(10)
    arrow.penup()
    arrow.fd(10)
    i += 1

myscreen2 = Screen()
myscreen2.exitonclick()

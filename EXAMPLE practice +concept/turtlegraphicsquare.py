from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("Red")
print(timmy)
for i in range(4):  # this draws a square
    timmy.forward(100)
    timmy.left(90)

myscreen = Screen()
myscreen.exitonclick()


# from turtle import *      # BY THIS YOU CAN IMPORT ALL THE PACKAGES IN PYTHON BUT NOT ADVISED TO DO IT AS THE CODE WILL NO LPNGER REMAIN READABLE

# import turtle
# t=turtle.Turtle()
# print(t)          #can do like this to import Turtle from package turtle

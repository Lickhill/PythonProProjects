from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)
userguess = screen.textinput(
    title="Choose a color.", prompt="Who do you think will win the race?"
)
print(f"The User bets on {userguess} turtle")
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
turtles = []


for i in range(7):
    timmy = Turtle(shape="turtle")
    timmy.color(colors[i])
    timmy.penup()
    timmy.speed(0)
    timmy.goto(-220, -180 + 60 * i)
    turtles.append(timmy)
count = 0
while True:
    for turtle in turtles:
        turtle.forward(random.randint(0, 11))
        if turtle.xcor() >= 220:
            if turtle.color()[0] == userguess:
                print(f"You've won. The winner is {turtle.color()[0]} turtle")
                count = 1
                break
            else:
                print(f"You've lost. The winner is {turtle.color()[0]} turtle")
                count = 1
                break
    if count == 1:
        break


screen.mainloop()

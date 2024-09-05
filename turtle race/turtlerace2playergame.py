from turtle import Turtle, Screen

eren = Turtle()
mikasa = Turtle()
eren.shape("turtle")
mikasa.shape("turtle")
eren.color("black")
mikasa.color("red")
eren.penup()
mikasa.penup()
eren.shapesize(1.4)
mikasa.shapesize(1.4)
eren.goto(-400, 50)
mikasa.goto(-400, -50)


def erenforward():
    eren.fd(50)
    checkposition()


def mikasaforward():
    mikasa.fd(50)
    checkposition()


def checkposition():
    if eren.xcor() == 400:
        print("black wins")
        myscreen.mainloop()

    elif mikasa.xcor() == 400:
        print("red wins")
        myscreen.mainloop()

    else:
        return


myscreen = Screen()
myscreen.listen()

myscreen.onkey(erenforward, "a")
myscreen.onkey(mikasaforward, "l")


myscreen.mainloop()

import colorgram
from turtle import Turtle, Screen

imagelocation = r"C:\coding projects\python\dotdrawingturtlegraphic.py\image.jpg"
colors = colorgram.extract(imagelocation, 100)

colorslist = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    colorslist.append((r, g, b))

print(colorslist)


circle = Turtle()
circle.shape("circle")
circle.shapesize(0.5)
myscreen = Screen()
myscreen.colormode(255)
myscreen.bgcolor("light yellow")
circle.penup()
circle.speed(0)

circle.setheading(135)
circle.fd(300)
# # Get the current turtle position
# x = circle.xcor()
# y = circle.ycor()
# print(x)
# print(y)

# # Set the new origin as the current position
# circle.setx(0)
# circle.sety(0)

circle.setheading(0)


count = 1
for j in range(10):
    for i in range(10):
        circle.pendown()
        circle.color(colorslist[count])
        circle.dot(15)
        circle.penup()
        circle.fd(44)
        count += 1
        if count == len(colorslist):
            count = 1

    circle.penup()
    circle.goto(-212.13203435596424, -40 * (j + 1) + 212.13203435596424)

circle.color("light yellow")
myscreen.mainloop()

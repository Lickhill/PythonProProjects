from turtle import Screen
from player import Player
from level import Level
from cars import Cars
import time

screen = Screen()
screen.setup(height=500, width=500)
screen.title("Cross The Road")
screen.bgcolor("white")

player = Player()
level = Level()
cars = Cars()

screen.tracer(0)

screen.listen()
screen.onkey(player.forward, "w")
screen.onkey(player.backward, "s")
screen.onkey(player.left, "a")
screen.onkey(player.right, "d")


gameon = True
while gameon:
    screen.update()
    time.sleep(0.03)
    if player.ycor() >= 230:
        level.inclevel()
        player.reset()
        cars.carmovedist += 2

    for vehicle in cars.gadi:
        if player.distance(vehicle) < 18:
            gameon = False
            level.gameover()

    cars.spawnthecars()
    cars.movecar()


screen.exitonclick()

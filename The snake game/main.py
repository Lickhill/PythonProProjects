from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

# import time
score = Score()
screen = Screen()
food = Food()
snake = Snake(screen)


screen.title("My Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(snake.left, "a")
screen.onkey(snake.up, "w")
screen.onkey(snake.right, "d")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
gaem_is_on = True
while gaem_is_on:
    screen.update()
    snake.forward()

    if snake.head.distance(food) < 20:
        snake.extend()
        food.refresh()
        score.refresh_and_inc()

    if snake.squares[0].ycor() > 280 or snake.squares[0].ycor() < -280:
        score.gameover()
        gaem_is_on = False

    for i in range(1, len(snake.squares)):
        if snake.squares[0].distance(snake.squares[i]) < 10:
            gaem_is_on = False
            score.gameover()

    screen.ontimer(snake.forward(), 70)

screen.exitonclick()

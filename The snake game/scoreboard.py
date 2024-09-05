from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.speed(0)
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.write(f"Score:{self.score}", align="center", font=("Ariel", 17, "normal"))

    def refresh_and_inc(self):
        self.score += 1
        self.clear()
        self.write(f"Score:{self.score}", align="center", font=("Ariel", 17, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Ariel", 24, "normal"))

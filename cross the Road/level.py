from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("black")
        self.goto(-190, 220)
        self.write(
            f"Level: {self.score}",
            align="center",
            font=("Copperplate Gothic Light", 14, "bold"),
        )

    def inclevel(self):
        self.clear()
        self.score += 1
        self.write(
            f"Level: {self.score}",
            align="center",
            font=("Copperplate Gothic Light", 14, "bold"),
        )

    def gameover(self):
        self.goto(0, 0)
        self.write(
            f"Game Over",
            align="center",
            font=("Copperplate Gothic Light", 20, "bold"),
        )

from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-270, 250)
        self.write(f"Score: {self.score}", font=FONT)

    def score_update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", font=FONT)
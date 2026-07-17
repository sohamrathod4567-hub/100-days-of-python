from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score =0
        self.goto(0,260)
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))



    def increase(self):
        self.score += 1
        self.clear()
        self.goto(0,260)
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))



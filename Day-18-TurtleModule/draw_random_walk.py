import turtle
from turtle import Turtle,Screen
import random
def random_color():
    r = random.randint (0,255)
    g = random.randint (0,255)
    b = random.randint (0,255)
    color = ( r, g, b )
    return color
angles = [0, 45, 90, 135, 180, 225, 270, 315]
tim = Turtle()
screen = Screen()
tim.pensize(15)
turtle.colormode(255)
screen.bgcolor("black")
for _ in range(200):
    tim.color(random_color())
    tim.forward(50)
    tim.setheading(random.choice(angles))

screen.exitonclick()
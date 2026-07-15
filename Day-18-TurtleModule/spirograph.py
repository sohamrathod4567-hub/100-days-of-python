import turtle as t
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
tim.speed("fastest")
screen = Screen()
tim.pensize(2)
t.colormode(255)
screen.bgcolor("black")
for i in range(200):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(i*3)

screen.exitonclick()
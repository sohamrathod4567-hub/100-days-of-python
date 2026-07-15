import turtle as t
from turtle import Turtle,Screen
import random
def random_color():
    r = random.randint (0,255)
    g = random.randint (0,255)
    b = random.randint (0,255)
    color = ( r, g, b )
    return color
tim = Turtle()
tim.speed("fastest")
screen = Screen()
tim.pensize(2)
t.colormode(255)
x = -350
y = -320
for _ in range(10):
    tim.penup()
    tim.goto( x  , y)
    tim.pendown()

    for i in range(10):

        tim.fillcolor(random_color())
        tim.begin_fill()
        tim.circle(10)
        tim.end_fill()
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    y += 50
    tim.pendown()




screen.exitonclick()
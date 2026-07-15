from importlib import import_module
from turtle import Turtle,Screen

tim = Turtle()

tim.shape("turtle")
tim.color("red")
tim.forward(100)
tim.color("blue")
tim.right(90)
tim.forward(100)
tim.color("green")
tim.right(90)
tim.forward(100)
tim.color("yellow")
tim.right(90)
tim.forward(100)

screen = Screen()
screen.exitonclick()

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(20)
def move_left():
    tim.left(20)
def move_right():
    tim.right(20)
def move_back():
    tim.back(20)
def clear():
    tim.penup()
    tim.goto(0,0)
    tim.pendown()
    tim.clear()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
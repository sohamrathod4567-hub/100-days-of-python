from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()


for _ in range(3):
    #For Triangle
    tim.color("purple")
    tim.forward(100)
    tim.right(120)

for _ in range(4):
    #For Square
    tim.color("green")
    tim.forward(100)
    tim.right(90)
for _ in range(5):
    #For pentagon
    tim.color("skyblue")
    tim.forward(100)
    tim.right(72)
for _ in range(6):
    #For hexagon
    tim.color("yellow")
    tim.forward(100)
    tim.right(60)
for _ in range(7):
    #For heptagon
    tim.color("red")
    tim.forward(100)
    tim.right(51.43)
for _ in range(8):
    #For octagon
    tim.color("orange")
    tim.forward(100)
    tim.right(45)
for _ in range(9):
    #For nonagon
    tim.color("gray")
    tim.forward(100)
    tim.right(40)
for _ in range(10):
    #For decagon
    tim.color("brown")
    tim.forward(100)
    tim.right(36)




screen.exitonclick()
from turtle import Turtle,Screen
import random
colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "black",
    "white",
    "gray",
    "cyan",
    "magenta",
    "gold",
    "silver",
    "navy",
    "teal",
    "lime",
    "maroon",
    "olive",
    "coral",
    "turquoise",
    "violet",
    "indigo",
    "khaki",
    "salmon",
    "plum",
    "orchid",
    "tan",
    "beige",
    "chocolate",
    "crimson",
    "darkgreen",
    "darkblue",
    "darkred",
    "darkorange",
    "darkviolet",
    "deepskyblue",
    "dodgerblue",
    "firebrick",
    "forestgreen",
    "hotpink",
    "lavender",
    "lightblue",
    "lightgreen",
    "mediumorchid",
    "midnightblue",
    "springgreen",
    "tomato",
    "wheat"
]
angles = [0, 45, 90, 135, 180, 225, 270, 315]
tim = Turtle()
screen = Screen()
tim.pensize(15)

def random_walk(disha,pen_color):

        tim.color(pen_color)
        tim.setheading(disha)
        tim.forward(50)

while True:
    turn = random.choice(angles)
    c = random.choice(colors)
    random_walk( turn, c )

screen.exitonclick()
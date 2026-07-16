import turtle
from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your Bet" , prompt=" Which turtle will win the race? Enter a color : ")
print(f"Your choice is : {user_bet}")
colors = ["red" , "orange" , "yellow", "blue" , "purple" , "green"]
y_positions = [-70 , - 40 , -10 , 20 , 50 , 80 ]
all_turtles = []
for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y= y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 215:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! {winning_color} wins")
            else:
                print(f"You lose!{winning_color} wins")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
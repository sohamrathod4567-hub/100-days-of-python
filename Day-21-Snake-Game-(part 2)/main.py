from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Scoreboard

game_is_on = True
screen =Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake-Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left , "a")
screen.onkey(snake.down , "s")
screen.onkey(snake.right , "d")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        print("Nom nom nom")
        score.increase()

    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        game_is_on = False
        score.game_over()


        #Detect collision with the snake body
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()






screen.exitonclick()
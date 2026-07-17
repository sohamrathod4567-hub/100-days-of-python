from turtle import Screen
import time
from snake import Snake

game_is_on = True
screen =Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake-Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left , "a")
screen.onkey(snake.down , "s")
screen.onkey(snake.right , "d")

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()



















screen.exitonclick()
import time
from turtle import Screen

from player import Player
from car_manager import CarManager
import random
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if random.randint(1, 6) == 1:
        cars.create_cars()

    cars.move_cars()

    if player.level_up():
        scoreboard.score_update()
        cars.speed_up()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.gameover()
            game_is_on = False

screen.exitonclick()
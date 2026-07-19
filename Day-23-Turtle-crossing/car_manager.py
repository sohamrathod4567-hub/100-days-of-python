from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_cars()
        self.starting_speed = STARTING_MOVE_DISTANCE
        self.speedup = MOVE_INCREMENT


    def create_cars(self) :
        new_car = Turtle()
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1 , stretch_len=2)
        new_car.goto(280, random.randint(-250, 250))
        self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.starting_speed)


    def speed_up(self):
        self.starting_speed += self.speedup

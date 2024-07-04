from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 4


class CarManager:
    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def create_cars(self):
        if random.randint(1, 4) == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.goto(280, random.randint(-250, 250))
            new_car.color(random.choice(COLORS))
            new_car.left(180)
            new_car.shapesize(stretch_len=2)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.move_distance)

    def check_level(self, level):
        self.move_distance += MOVE_INCREMENT*level

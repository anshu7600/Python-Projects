from turtle import Turtle
from random import choice
import time

SPEED = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.options = [SPEED, -SPEED]
        self.y = choice(self.options)
        self.x = choice(self.options)

    def move_ball(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y *= -1

    def x_bounce(self):
        self.x *= -1

    def refresh(self):
        self.goto(0, 0)
        self.y = choice(self.options)
        self.x = choice(self.options)
        time.sleep(1)

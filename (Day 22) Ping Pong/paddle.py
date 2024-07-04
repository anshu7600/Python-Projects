from turtle import Turtle
MOVE_DISTANCE = 25


class Paddle(Turtle):
    def __init__(self, coordinates, screen_height):
        super().__init__()
        self.coordinates = coordinates
        self.make_paddle()
        self.screen_height = screen_height
        
    def make_paddle(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=5)
        self.goto(self.coordinates)
        self.left(90)

    def paddle_up(self):
        if self.screen_height / 2 - 70 > self.ycor():
            self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def paddle_down(self):
        if self.ycor() > -self.screen_height / 2 + 70:
            self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
        
        
import time
from turtle import Turtle

SNAKE_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self, shape, color):
        self.turtle_squares = []
        self.shape = shape
        self.color = color
        self.create_snake()
        self.first_piece = self.turtle_squares[0]

    def create_snake(self):
        for turtle_position_x in SNAKE_POSITION:
            new_turtle = Turtle(shape=self.shape)
            new_turtle.color(self.color)
            new_turtle.penup()
            new_turtle.goto(turtle_position_x)
            self.turtle_squares.append(new_turtle)

    def extend_snake(self):
        new_turtle = Turtle(shape=self.shape)
        new_turtle.color(self.color)
        new_turtle.penup()
        self.turtle_squares.append(new_turtle)

    def reset_snake(self):
        for turtle in self.turtle_squares:
            turtle.goto(2000, 2000)
        self.turtle_squares.clear()
        self.create_snake()
        self.first_piece = self.turtle_squares[0]

    def move_forward(self):
        for square_number in range(len(self.turtle_squares) - 1, 0, -1):
            new_x = self.turtle_squares[square_number - 1].xcor()
            new_y = self.turtle_squares[square_number - 1].ycor()
            self.turtle_squares[square_number].goto(new_x, new_y)
        self.first_piece.forward(MOVE_DISTANCE)

    def up(self):
        if self.first_piece.heading() != DOWN:
            self.first_piece.setheading(UP)

    def down(self):
        if self.first_piece.heading() != UP:
            self.first_piece.setheading(DOWN)

    def right(self):
        if self.first_piece.heading() != LEFT:
            self.first_piece.setheading(RIGHT)

    def left(self):
        if self.first_piece.heading() != RIGHT:
            self.first_piece.setheading(LEFT)

    def game_over_blink(self, screen):
        screen.tracer(0)
        for i in range(2):
            for turtle_piece in self.turtle_squares:
                turtle_piece.ht()
            time.sleep(0.5)
            screen.update()
            for turtle_piece in self.turtle_squares:
                turtle_piece.st()
            time.sleep(0.5)
            screen.update()

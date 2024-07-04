import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player_turtle = Player()
score_board = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkeypress(key="Up", fun=player_turtle.move_forward)
screen.onkeypress(key="w", fun=player_turtle.move_forward)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move_cars()

    if player_turtle.ycor() >= 280:
        player_turtle.reset_turtle()
        cars.check_level(score_board.write_level())

    for car in cars.all_cars:
        if player_turtle.distance(car) < 25:
            score_board.game_over()
            game_is_on = False

screen.exitonclick()

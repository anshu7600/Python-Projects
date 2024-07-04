import time
from snake import Snake
from turtle import Screen
from extra import Extra
from food import Food
from scoreboard import Scoreboard

screen = Screen()
extra_class = Extra(screen)
snake = Snake(shape="square", color="white")

extra_class.screen_setup()
extra_class.ask_prompt()
food = Food()
scoreboard = Scoreboard()
extra_class.listen_keys(snake)


def game_over():
    scoreboard.game_over()
    food.remove_food()
    snake.game_over_blink(screen)
    scoreboard.reset_scoreboard()
    snake.reset_snake()
    time.sleep(1.5)
    food.refresh()
    food.show_food()

time.sleep(1)
game_is_on = True
while game_is_on:
    snake.move_forward()
    screen.update()
    time.sleep(extra_class.difficulty_number)

    if snake.first_piece.distance(food) < 16:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()

    elif snake.first_piece.xcor() > 280 or snake.first_piece.xcor() < -280 or snake.first_piece.ycor() > 280 or \
    snake.first_piece.ycor() < -280:
        game_over()

    for piece in snake.turtle_squares[1:]:
        if snake.first_piece.distance(piece) < 10:
            game_over()

screen.exitonclick()

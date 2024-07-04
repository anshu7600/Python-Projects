import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen_width = 1200
screen_height = 600
screen.setup(width=screen_width, height=screen_height)
screen.title("Ping Pong 2")
screen.tracer(0)

right_paddle = Paddle((screen_width/2-50, 0), screen_height)
left_paddle = Paddle((-screen_width/2+50, 0), screen_height)
score = Scoreboard(screen_height, screen_width)
score.make_left_score()
score.make_right_score()
ball = Ball()

screen.listen()
screen.onkeypress(key="Up", fun=right_paddle.paddle_up)
screen.onkeypress(key="Down", fun=right_paddle.paddle_down)
screen.onkeypress(key="w", fun=left_paddle.paddle_up)
screen.onkeypress(key="s", fun=left_paddle.paddle_down)

game_is_on = True
while score.check_score():
    screen.update()
    time.sleep(0.07)
    ball.move_ball()

    if ball.ycor() > screen_height/2-20 or ball.ycor() < -screen_height/2+20:
        ball.y_bounce()
    elif ball.distance(left_paddle) < 60 and ball.xcor() == -screen_width/2+60 or ball.distance(right_paddle) < 60 and \
            ball.xcor() == screen_width/2-60:
        ball.x_bounce()
    elif ball.xcor() > screen_width/2+15:
        ball.refresh()
        score.update_left_score()
    elif ball.xcor() < -screen_width/2-15:
        ball.refresh()
        score.update_right_score()


screen.exitonclick()

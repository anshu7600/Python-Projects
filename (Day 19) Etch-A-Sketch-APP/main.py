from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def tilt_right():
    tim.right(10)

def tilt_left():
    tim.left(10)

def clear_screen():
    tim.clear()

def go_home():
    tim.pu()
    tim.home()
    tim.pd()

screen.listen()
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_backwards)
screen.onkey(key="Right", fun=tilt_right)
screen.onkey(key="Left", fun=tilt_left)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="h", fun=go_home)

screen.exitonclick()

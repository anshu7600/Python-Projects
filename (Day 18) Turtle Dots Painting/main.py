import turtle
from turtle import Turtle, Screen
from random import randint

tingu_the_turtle = Turtle()
turtle.colormode(255)


def random_color():
    tingu_the_turtle.color((randint(0, 255), randint(0, 255), randint(0, 255)))

# tingu_the_turtle.shape("turtle")
# tingu_the_turtle.color("blue")
# tingu_the_turtle.width(10)
#
# for i in range(4):
#     tingu_the_turtle.forward(240)
#     tingu_the_turtle.right(90)

for i in range(24):
    tingu_the_turtle.pendown()
    tingu_the_turtle.forward(10)
    tingu_the_turtle.penup()
    tingu_the_turtle.forward(10)

color_list = ["red", "green", "blue", "blue1", "cyan", "brown", "yellow", "orange"]
# sides = 3
# for i in range(7):
#     tingu_the_turtle.color(color_list[randint(0, len(color_list))])
#     angle = 360/sides
#     for _ in range(sides):
#         tingu_the_turtle.forward(100)
#         tingu_the_turtle.right(angle)
#     sides += 1

# tingu_the_turtle.width(14)
# angle_options = [90, 180, 270, 0]
# tingu_the_turtle.speed(0)
# for i in range(240):
#     random_color()
#     # tingu_the_turtle.color(color_list[randint(0, len(color_list)-1)])
#     tingu_the_turtle.forward(30)
#     tingu_the_turtle.right(angle_options[randint(0, 3)])

# tingu_the_turtle.speed(0)
# def draw_something(size_of_gap):
#     for i in range(int(360/size_of_gap)):
#         random_color()
#         tingu_the_turtle.circle(100)
#         tingu_the_turtle.right(size_of_gap)
# draw_something(1)


screen = Screen()
screen.exitonclick()

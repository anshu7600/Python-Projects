import turtle
import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract("hirst_painting.jpg", 100)

tom = Turtle()
rgb_list = []
turtle.colormode(255)
for i in range(len(colors)):
    rgb_list.append(colors[i].rgb)

tom.hideturtle()
tom.speed("fastest")
tom.penup()
tom.back(225)
tom.left(90)
tom.back(225)
tom.right(90)
for i in range(10):
    for _ in range(10):
        tom.color(random.choice(rgb_list))
        tom.begin_fill()
        tom.circle(10)
        tom.end_fill()
        tom.fd(50)
    tom.left(90)
    tom.fd(50)
    tom.right(90)
    tom.back(500)

screen = Screen()
screen.exitonclick()

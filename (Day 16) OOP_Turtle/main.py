from turtle import *
import prettytable

# the_turtle = Turtle()
# the_turtle.shape("circle")
# the_turtle.color("cyan")
# the_turtle.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()

table = prettytable.PrettyTable()
table.field_names = ["Pokemon", "Type"]
table.add_rows([
    ["Pikachu", "Electric"],
    ["Charmander", "Fire"],
    ["Grininja", "Water"]
])
table.align = "l"

print(table)

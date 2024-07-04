import random
from turtle import Turtle, Screen
from movement_odds import MovementOdds

is_race_on = False
right_option = True
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = None

screen = Screen()
screen.setup(width=500, height=400)

while right_option:
    user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a Color: ")
    if user_bet not in colors:
        print("Wrong option \n")
    else:
        right_option = False
user_money_bet = screen.textinput(title="Bet Some MONEY!", prompt="How much money do you bet: ")
if user_money_bet.lower() in ["no", "none", "0"]:
    print("Not betting any Money? WHY?")
    print("")

all_turtles = []
y_value = -60
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_value)
    y_value += 25
    all_turtles.append(new_turtle)

if user_bet.lower() in colors and user_money_bet:
    is_race_on = True

turtle_movement_odds = MovementOdds().turtle_movement_odds
while is_race_on and not right_option:
    for turtle in all_turtles:
        random_distance = random.choice(turtle_movement_odds)
        turtle.forward(random_distance)
        if turtle.xcor() > 225:
            print(f"{str(turtle.color()[0]).title()} won the race!")
            if user_bet.lower() == turtle.color()[0]:
                print("You win!")
                print(f"You win {int(user_money_bet) * 2}")
            else:
                print("Wrong Choice.")
            is_race_on = False


screen.exitonclick()

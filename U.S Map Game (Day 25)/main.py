import turtle
import pandas

screen = turtle.Screen()
screen.setup(725, 491)
screen.title("U.S. Sates Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()
write_turtle = turtle.Turtle()
write_turtle.penup()
write_turtle.hideturtle()

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

correct_guesses = []

while len(correct_guesses) != 50:
    answer_state = screen.textinput(title=f"Guessed {len(correct_guesses)}/50 Correct",
                                    prompt="What's another state's name?").title()
    if answer_state.title() == "Exit":
        break
    if answer_state in states_list:
        correct_guesses.append(answer_state)
        state_info = data[data.state == answer_state]
        write_turtle.goto(int(state_info.x), int(state_info.y))
        write_turtle.write(answer_state)
    elif answer_state.title() == "Reset":
        correct_guesses = []
        write_turtle.clear()
        continue

data_dict = {"states": [state for state in states_list if state not in correct_guesses]}
df = pandas.DataFrame(data_dict)
df.to_csv("states_to_learn.csv")

write_turtle.goto(x=-190, y=0)
if len(correct_guesses) == 1:
    write_turtle.write("Guessed All of States Right 😎😎", font=("Arial", 20, "bold"))
else:
    write_turtle.write("Learn, and be back to take rock!", font=("Arial", 20, "bold"))

screen.exitonclick()

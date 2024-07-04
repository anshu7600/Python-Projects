import turtle
import pandas

screen = turtle.Screen()
screen.setup(745, 868)
screen.title("India Sates Game")
image = "india_blank_states_map.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()
write_turtle = turtle.Turtle()
write_turtle.penup()
write_turtle.hideturtle()

data = pandas.read_csv("28_states.csv")
states_list = data.state.to_list()

correct_guesses = []

while len(correct_guesses) != 28:
    answer_state = screen.textinput(title=f"Guessed {len(correct_guesses)}/28 Correct",
                                    prompt="What's another state's name?").title()
    if answer_state.title() == "Exit":
        break
    elif answer_state in states_list:
        correct_guesses.append(answer_state)
        state_info = data[data.state == answer_state]
        write_turtle.goto(int(state_info.x.iloc[0]), int(state_info.y.iloc[0]))
        write_turtle.write(answer_state)
    elif answer_state.title() == "Reset":
        correct_guesses = []
        write_turtle.clear()
        continue

data_dict = {"states": [state for state in states_list if state not in correct_guesses]}
df = pandas.DataFrame(data_dict)
df.to_csv("states_to_learn.csv")

write_turtle.goto(x=-190, y=0)
if len(correct_guesses) == 28:
    write_turtle.write("Guessed All of States Right 😎😎", font=("Arial", 20, "bold"))
else:
    write_turtle.write("Learn, and be back to rock!", font=("Arial", 20, "bold"))

screen.exitonclick()

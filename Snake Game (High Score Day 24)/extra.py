import tkinter.messagebox


class Extra:
    def __init__(self, screen):
        self.difficulty_number = .1
        self.screen = screen

    def ask_prompt(self):
        difficulty = self.screen.textinput(prompt="What difficulty do you choose: Impossible, Hard or Easy",
                                           title="Difficulty") \
            .lower()
        options = ["hard", "easy", "impossible"]
        if difficulty in options:
            if difficulty == "hard":
                self.difficulty_number = .03
            elif difficulty == "impossible":
                self.difficulty_number = .015
            elif difficulty == "easy":
                self.difficulty_number = 1
                tkinter.messagebox.showinfo(title="Me Personally", message="Damm, Like imagine being that trash.")
            else:
                self.difficulty_number = .1
        else:
            try:
                self.difficulty_number = int(difficulty)
            except ValueError:
                pass

    def screen_setup(self):
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("SNAKE GAME @>)")
        self.screen.tracer(0)

    def listen_keys(self, snake):
        self.screen.listen()
        self.screen.onkey(key="Up", fun=snake.up)
        self.screen.onkey(key="Down", fun=snake.down)
        self.screen.onkey(key="Left", fun=snake.left)
        self.screen.onkey(key="Right", fun=snake.right)
        self.screen.onkey(key="w", fun=snake.up)
        self.screen.onkey(key="s", fun=snake.down)
        self.screen.onkey(key="a", fun=snake.left)
        self.screen.onkey(key="d", fun=snake.right)

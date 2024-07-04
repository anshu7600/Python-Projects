from turtle import Turtle
import time
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        try:
            with open("data") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            with open("data", mode="w") as file:
                file.write("0")
            with open("data") as file:
                self.high_score = int(file.read())
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.ht()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
        self.goto(0, 260)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data", mode="w") as file:
            print(self.high_score)
            file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

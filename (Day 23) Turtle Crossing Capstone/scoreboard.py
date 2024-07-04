from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 0
        self.goto(-280, 260)
        self.hideturtle()
        self.write_level()

    def write_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)
        return self.level

    def game_over(self):
        self.goto(-70, -20)
        self.write("Game Over", font=FONT)

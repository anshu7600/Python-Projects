from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, screen_height, screen_width):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.create_dotted_line(screen_height)
        self.left_score = 0
        self.right_score = 0

    def create_dotted_line(self, screen_height):
        y = -screen_height/2+20
        for _ in range(int(screen_height/40)):
            new_turtle = Turtle("square")
            new_turtle.penup()
            new_turtle.shapesize(stretch_len=2, stretch_wid=.7)
            new_turtle.left(90)
            new_turtle.color("white")
            new_turtle.goto(0, y)
            y += 80

    def make_left_score(self):
        self.hideturtle()
        position_x = -self.screen_width/2 + (self.screen_width/2-100)
        position_y = self.screen_height/2 - 125
        self.color("white")
        self.penup()
        self.goto(position_x, position_y)
        self.write(f"{self.left_score}", font=("Arial", 80, "normal"))

    def make_right_score(self):
        self.hideturtle()
        position_x = self.screen_width/2 - (self.screen_width/2-45)
        position_y = self.screen_height/2 - 125
        self.color("white")
        self.penup()
        self.goto(position_x, position_y)
        self.write(f"{self.right_score}", font=("Arial", 80, "normal"))

    def update_right_score(self):
        self.clear()
        self.right_score += 1
        self.make_right_score()
        self.make_left_score()

    def update_left_score(self):
        self.clear()
        self.left_score += 1
        self.make_right_score()
        self.make_left_score()

    def check_score(self):
        if self.right_score == 5:
            self.goto(self.screen_width / 2 / 2 - 30, -30)
            self.write("Win", font=("Arial", 60, "normal"))
            return False
        elif self.left_score == 5:
            self.goto(-self.screen_width / 2 / 2 + 30, -30)
            self.write("Win", font=("Arial", 60, "normal"))
            return False
        else:
            return True

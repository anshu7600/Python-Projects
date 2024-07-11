from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain, category: str):
        self.quiz = quiz_brain
        self.category = category

        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=40, pady=40)
        self.window.title("Quizzer")

        self.category_label = Label(text=f"{self.category}", fg="white", font=("Arial", 15, "normal"), bg=THEME_COLOR)
        self.category_label.grid(row=0, column=0)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", font=("Arial", 15, "normal"),
                                 bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)

        self.question_canvas = self.canvas.create_text(150, 125, text="", font=("Arial", 15, "italic"), width=270)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, relief=FLAT, bd=0, highlightthickness=0,
                                  command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, relief=FLAT, bd=0, highlightthickness=0,
                                   command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_canvas, text=question_text)
        else:
            self.canvas.itemconfig(self.question_canvas, text="You have reached the end of the quiz.",
                                   font=("Arial", 15, "normal"), )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        self.score_label.config(text=f"Score: {self.quiz.score}")

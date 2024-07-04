from question_model import *
from data import *
from quiz_brain import *

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("\nYou have finished the quiz!")
print(f"Your final score is {quiz_brain.score}/{quiz_brain.question_number}")

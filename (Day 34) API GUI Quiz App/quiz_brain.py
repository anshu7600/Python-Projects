import html

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.current_question = None

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        if self.question_number != 1:
            print("")
        unescaped_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {unescaped_text}"
        # user_answer = input(f"Q.{self.question_number}: {unescaped_text} (True/False): ")
        # self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

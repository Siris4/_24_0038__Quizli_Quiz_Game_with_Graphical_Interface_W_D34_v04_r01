import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0   # get the value from here, then populate it into the UI.py file, everytime we get the next question.
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text} (True/False): " # <-- we change the code here because that's where we format it into our user answer
        # here below, we want to Output that text into our ui.py file (which we can start doing, by returning that f-string above.
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")  # remove this from the middle section of this line, and place q_text instead
        # self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
            print("You got it right!")
        else:
            return False
            print("That's wrong.")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")



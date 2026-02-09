class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} : {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)  # Correctly accessing 'answer'

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


# This class controls the flow of the quiz game. It has the following components:
#
# __init__(self, q_list): Initializes the quiz with a list of Question objects. It also initializes the question_number (to track which question
# is currently being asked) and score (to track the user's score).
#
# still_has_questions(self): Returns True if there are more questions to ask, and False if the quiz is over.
#
# next_question(self): This method gets the next question, increments the question number, asks the user for an answer (via input()),
# and then checks if the answer is correct by calling check_answer().
#
# check_answer(self, user_answer, correct_answer): This method compares the user s input with the correct answer.
#  If the answer is correct, the score is incremented, and feedback is provided to the user (whether they were right or wrong).
#  It also prints the correct answer and the user s current score.
class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer  # Make sure this is 'answer'

#The Question class represents a single question in the quiz. Each Question object has
# two attributes:
#
# text: The question text.
# answer: The correct answer.
# When a new Question object is created, it is initialized with these values.
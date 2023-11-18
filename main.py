from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_banck = []

for question in question_data:
    question_banck.append(Question(question["text"], question["answer"]))

quiz = QuizBrain(question_banck)

while quiz.still_has_gestions():
    quiz.next_guestion()
print("You've completed the quezs.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")

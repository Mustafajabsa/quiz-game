class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_gestions(self): 
        return self.question_number < len(self.question_list)
    def check_answer(self, answer, correct_answer):
            '''comparing the two answers and return true or false'''
            if answer.lower() == correct_answer.lower():
                self.score += 1
                print("you got it right")
            else:
                print("that was werong!!")
            print(f"the correct answer is {correct_answer}")
            print(f"your current score is {self.score}/{self.question_number}")
            print("\n")

    def next_guestion(self):
        '''retreive the item
        at the current question number from the question list'''
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number} : {current_question.text} (True/False).")
        self.check_answer(answer, current_question.answer)

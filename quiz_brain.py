class QuizBrain:
    
    # Initialize the game.
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = q_list

    # Assess how many questions are left of the quiz to continue game.
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)  # Also means True
        # ^ Above is a simplified version of this boolean statement
        # if self.question_number < len(self.questions_list):
        #     return True
        # else return False

    # Ask the user questions, check it, and move on to the next.
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    # Checking if the answer was correct.
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.\n")
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# Iterate over question data to create a Question object and append to the question_bank/
for question_dict in question_data:
    question_text = question_dict["question"]
    question_answer = question_dict["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

# Instantiate quiz to begin game.
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")

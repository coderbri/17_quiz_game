# Todo List

## Setting up the Data, Model and Main Game Logic

- [x]  1. Create a Question Class with an `__init__()` method with two attributes: text and answer (**question_model.py**).
- [x]  2. Import `question_data` and `Question` model files (**main.py**).
- [x]  3. Write a for loop to iterate over the question_data. There are 12 dicts in the `question_data` list (**main.py**).
- [x]  4. Create a `Question` object from each entry in `question_data` (**main.py**).
- [x]  5. Append each `Question` object to the `question_bank` (**main.py**).

## Setting up the Quiz Game Model

- [x]  7. Write an `__init__()` method (**quiz_brain.py**).
- [x]  8. Initialize the `question_number` to 0 (**quiz_brain.py**).
- [x]  9. Initialize the `question_list` to an input (**quiz_brain.py**).
- [x]  10. Ask the question. Retrieve the item at the current `question_number` from the `question_list`. Use the `input()` function to show the user the Question "text" and ask for the user's "answer".
- [x]  11. Import `QuizBrain` and simulate the question prompt (**main.py**).
- [x]  12. Create a method called `still_has_questions()`. Return a boolean depending on teh value of `question_number`. Use the while loop to show the next question until the end (**quiz_brain.py**).
- [x]  13. Check if the user's answer was correct (**quiz_brain.py**).
- [x]  14. Let the user know they finished the quiz and what their final score was (**main.py**).

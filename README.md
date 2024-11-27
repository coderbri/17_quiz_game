# 17 Quiz Game

This project is the **Day 17 Challenge** of the *100 Days of Code: Python Pro Bootcamp* by Dr. Angela Yu. The goal was to deepen understanding of Python Object-Oriented Programming (OOP) principles while structuring and modularizing the code across multiple files.  

The game implements a simple True/False quiz that draws its questions from the [Open Trivia Database](https://opentdb.com/api_config.php), specifically from the Computer Science category.  


## Table of Contents
- [Features](#features)
- [Gameplay Flow - How It Works](#gameplay-flow---how-it-works)
- [Implementation Details](#implementation-details)
  - [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
  - [Game Logic](#game-logic)
- [How to Run](#how-to-run)
  - [Example Output](#example-output)


## Features
- **Object-Oriented Design**:
  - The game is designed using Python classes to encapsulate the `Question` objects and manage quiz functionality through the `QuizBrain` class.

- **Trivia Questions**:
  - Trivia questions are sourced from the Open Trivia Database and formatted for display. The project uses hardcoded data in `data.py`, but the setup can be adapted to dynamically fetch questions from the Open Trivia Database API.

- **Game Logic**: 
  - Players are presented with questions sequentially.  
  - Input is accepted as either `True` or `False`.  
  - Immediate feedback is provided after each question, showing whether the answer was correct.  
  - A score counter tracks the player's progress, and the final score is displayed at the end.


## Gameplay Flow - How It Works

1. **Setup**:
   - The `data.py` file contains trivia questions and answers in dictionary format.  
   - These are converted into `Question` objects and stored in a question bank (`question_bank`).  

2. **QuizBrain Class**:
   - The `QuizBrain` class is responsible for managing game logic:  
     - Tracking the current question number.  
     - Checking if more questions remain.  
     - Comparing the player's answers with the correct answers.  

3. **User Interaction**:
   - The game displays each question using the `next_question()` method.  
   - The user inputs their answer, and the program checks if it matches the correct answer using the `check_answer()` method.  

4. **End of Game**:  
   - When all questions are answered, the game displays the user's final score.



## Implementation Details

### Object-Oriented Programming (OOP):
- **`Question` Class**:  
  Encapsulates a single question and its corresponding correct answer.  
  ```python
  class Question:
      def __init__(self, q_text, q_answer):
          self.text = q_text
          self.answer = q_answer
  ```  

- **`QuizBrain` Class**:  
  Encapsulates the quiz logic and handles interaction with the player.  
  ```python
  class QuizBrain:
      def __init__(self, q_list):
          self.question_number = 0
          self.score = 0
          self.questions_list = q_list
      ...
  ```

### Game Logic:
- The game checks if there are remaining questions using the `still_has_questions()` method.  
- Each question is presented sequentially using `next_question()`.  
- Answers are validated using the `check_answer()` method, with feedback provided to the user.  


## How to Run

1. Clone this repository.
2. Run the program using Python.
3. Answer the questions by typing `True` or `False`. Enjoy the quiz!

---

### Example Output

```
Q.1: The Python programming language gets its name from the British comedy group "Monty Python." (True/False)?: True  
You got it right!  
The correct answer was: True.  
Your current score is 1/1.  

Q.2: The Windows ME operating system was released in the year 2000. (True/False)?: False  
That's wrong.  
The correct answer was: True.  
Your current score is 1/2.  

...  

You've completed the quiz!  
Your final score was: 8/10.
```


---
<section align="center">
  <code>coderBri © 2024</code>
</section>
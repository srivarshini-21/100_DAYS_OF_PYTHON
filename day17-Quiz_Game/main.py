from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[] # Empty list to store question objects
for question in question_data: # Acesses each dictionary in the list
    q_text=question['question'] # Key - question
    q_ans=question['correct_answer'] # Value - answer
    q_obj=Question(q_text,q_ans) # Passing the question and answer to the object as attributes - Question class defined in question_model.py
    question_bank.append(q_obj) # Add the created object to the list

quiz = QuizBrain(question_bank) # Create object for quiz question passing the question_bank list of question objects as argument
while quiz.still_has_questions(): # Until the question number is lesser than length of question_list
    quiz.next_question() # Access the method defined in the 'QuizBrain' class

print("Congratulations on completing the quiz! ")
print(f'Your final score is {quiz.score}/{quiz.question_num}')
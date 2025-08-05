from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[] # Empty list to store question objects
for question in question_data: # Acesses each dictionary in the list
    q_text=question['text'] # Key - question
    q_ans=question['answer'] # Value - answer
    q_obj=Question(q_text,q_ans) # Passing the question and answer to the object as attributes
    question_bank.append(q_obj) # Add the created object to the list

quiz = QuizBrain(question_bank) # Create object for quiz question
quiz.next_question() # Access the method defined in the 'QuizBrain' class
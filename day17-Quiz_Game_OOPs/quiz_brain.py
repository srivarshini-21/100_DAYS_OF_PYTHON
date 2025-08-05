class QuizBrain():
    def __init__(self,q_list):
        self.question_num=0 # Index starts from 0 to access the first question from the list
        self.question_list=q_list # List of questions in the question_bank

    def still_has_questions():
        pass

    def next_question(self):
        current_q=self.question_list[self.question_num]
        self.question_num+=1
        input(f"Q.{self.question_num}: {current_q.text} True or False?")

        
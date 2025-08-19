class QuizBrain():
    def __init__(self,q_list):
        self.question_num=0 # Index starts from 0 to access the first question from the list
        self.question_list=q_list # List of questions in the question_bank
        self.score=0

    def still_has_questions(self):
        return self.question_num<len(self.question_list) # Returns True if satisfies the condition else False
        

    def next_question(self):
        current_q=self.question_list[self.question_num]
        self.question_num+=1
        user_ans=input(f"Q.{self.question_num}: {current_q.text} (True/False?)")
        self.check_ans(user_ans,current_q.answer)

    def check_ans(self,user_ans,correct_answer):
        if user_ans.lower()==correct_answer.lower():
            print("You got it right!")
            self.score+=1
        else:
            print("You got it wrong.") 
        print(f"The correct answer was: {correct_answer}")   
        print(f"Your current score is: {self.score}/{self.question_num}")
        print("\n")


        
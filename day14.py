# Day 14 - Higher Or Lower Game
from higher_lower_data_day14 import logo, vs, data
import random
def format_data(acc):
    """Formats the data of accounts into printable format"""
    acc_name=acc['name']
    acc_desc=acc['description']
    acc_country=acc['country']
    return f"{acc['name']}, a {acc['description']}, from {acc['country']}"

def check_answer(user_guess, a_f, b_f):
    """Takes user input and follower counts and returns if they got it right """
    if a_f > b_f:
        return user_guess=="a"
    else:
        return user_guess=="b"
    # If acc1 followers are more than acc2 and the user guessed 'A' return True else i.e if acc2 followers are more than acc1 and the user guessed 'B' return True - User gained a point. If neither is True return False = User lost
score=0
game_over=False
print(logo)
acc2=random.choice(data) # After 1 round of correct guess the 
while game_over==False:
    
    acc1=acc2
    acc2=random.choice(data)
    if acc1 == acc2:
        acc2=random.choice(data)
    print(f"Compare A: {format_data(acc1)}")
    print(vs)
    print(f"Against B: {format_data(acc2)}")
    guess=input("Who has more followers? Type 'A' or 'B' : ").lower()

    print("\n" * 20)
    print(logo)

    a_follower_count=acc1['follower_count']
    b_follower_count=acc2['follower_count']

    is_correct= check_answer(guess,a_follower_count,b_follower_count)
    if is_correct:
            score+=1
            print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry that's wrong. Final score: {score}")
        game_over=True

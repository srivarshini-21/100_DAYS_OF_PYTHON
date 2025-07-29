# Day 12
a=1 # Global
def scope():
    a=2 # Local
    print(f"The value is : {a}")

scope()
print(f"The value outside is : {a}")

# No block scope in python example
level=3
if level<5:
    hard=50

print(hard) # Prints 50 even when the variable is defined inside 'if' block

# Prime number check
def is_prime(num):
    if num==2:
        return True
    if num==1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
        
    return True

# Modifying global scope variable 
enemies=1
def inc_enemies(enemy):
    print(f"Enemies inside function: {enemies}")
    return enemy+1

enemies=inc_enemies(enemies)
print(f"Enemies after increase: {enemies}")

# Day 12 Project - Guess the number
# Approach 1
import random
logo=r"""
   _____                        _______ _             _   _                 _               
  / ____|                      |__   __| |           | \ | |               | |              
 | |  __ _   _  ___  ___ ___      | |  | |__   ___   |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|     | |  | '_ \ / _ \  | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \     | |  | | | |  __/  | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/     |_|  |_| |_|\___|  |_| \_|\__,_|_| |_| |_|_.__/ \___|_|         
"""
print(logo)
print("\nWelcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100")
num=random.randint(1,100)
difficulty=input("Type 'easy or 'hard': ")
if difficulty=="easy":
    attempts=10
elif difficulty=="hard":
    attempts=5
game_over=False
while attempts>0 and game_over==False:
    while game_over==False:     
        print(f"You have {attempts} remaining to guess the number.")
        guess=int(input("Make a guess: "))
        if guess==num:
            print(f"You have got it! The answer was {num}")
            game_over=True
        elif guess>num:
            print("Too high.\nGuess again.")
            attempts-=1
        elif guess<num:
            print("Too low.\nGuess again.")
            attempts-=1
        if attempts==0:
            print("You have run out of guesses. Run again to play!")
            game_over=True

# Approach 2 - Using fucntions and return statements and gloabl and local variables
from random import randint
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
turns=0

def check_answer(guess,answer,turns):
     """Checks answer against guess and returns number of turns remaining"""
     if guess==answer:
            print(f"You have got it! The answer was {answer}")
     elif guess>answer:
        print("Too high.")
        return turns-1
     else:
        print("Too low.")
        return turns-1

def set_difficulty():
    level=input("Choose a difficulty. Type 'easy' or 'hard' : ")
    if level=='easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():    
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 to 100")
    num=randint(1,100)
    print(num)
    turns=set_difficulty()

    guess=0
    while guess!=num:
        print(f"You have {turns} remaining to guess the number.")
        guess=int(input("Make a guess: "))
        turns=check_answer(guess,num,turns)
        if turns==0:
            print("You have run out of guesses. Run again to play!")
            return
        elif guess!=num:
            print("Guess again.")

game()




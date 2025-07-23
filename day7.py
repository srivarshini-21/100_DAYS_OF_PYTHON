# Coding the Hangman Game
# Step 1: Picking random words and checking answers
from hangman_props import word_list,stages,logo
import random
lives=6
print(logo)
chosen_word=random.choice(word_list)
print(chosen_word)
placeholder=""  # Step 2: Replacing Blanks with guesses
for c in chosen_word:
    placeholder+="_ "
print("Your word to guess: ",placeholder)
game_over=False
correct_word=[]
while  not game_over:
    print(f"\n************************* {lives}/6 LIVES LEFT ***************************")
    guess=input("\nGuess a letter: ").lower()
    if guess in correct_word:
        print(f"You have already guessed {guess} ")
    display=""
    for c in chosen_word:
        if guess==c:
            display+=c  
            correct_word.append(c)     
        elif c in correct_word:
            display+=c     
        else:
            display+="_ "      
        # Step 2: Replacing Blanks with guesses

    if guess not in chosen_word:
        print("Wrong Guess! You lose a life :(")
        lives -= 1
        if lives==0:
            game_over=True
            print(f"***************** The word was {chosen_word}. YOU LOSE *****************")
    if "_" not in display:
        game_over=True
        print("********************* YOU WON! ************************") # Step 3: Checking if player has won
    print(stages[lives])
    print("Your word: ",display)
    

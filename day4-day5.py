# Day4
import random
print(random.randint(1,7))
print(random.random())
print(random.uniform(2,10))

rand_head_tail=random.randint(0,1)
if rand_head_tail==0:
    print("Heads")
else:
    print("Tails")

# Lists
states=["Karnataka","Tamil Nadu","Punjab","Gujarat"]
print(states[0])
states[2]="Kerala"
print(states)
states.append("Bihar")
print(states)
states.extend(["Rajastan","West Bengal","Andhra Pradesh"])
print(states)

# Who's gonna pay
ppl=['Alice','Bob','Charlie','David','Emanuel']
i=random.randint(0,4)
print(f"Person paying the bill: {ppl[i]}")

#Alt soln
print(random.choice(ppl))
# Acessing in nested lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])

# Day4 Project
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_img=[rock,paper,scissors]
player=int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors\n"))
if player>=3 or player<0:
    print("Invalid input. You lose!")
else:
    print(game_img[player])    

comp_choice=random.randint(0,2)
print(f"Computer chose:\n {game_img[comp_choice]}")
if player==comp_choice:
    print("It's a draw!")
elif player==0 and comp_choice==2:
    print("You win!")
elif player ==2 and comp_choice==0:
    print("You lose!")
elif player<comp_choice:
    print("You lose!")
elif player>comp_choice:
    print("You win!")

#Day5
letters=["a","b","c","d"]
for letter in letters:
    print("This is "+letter)

scores=[34,45,67,687,93,12,33,77,123,1]
sum=0
for score in scores:
    sum+=score
print(sum)

max=0
for score in scores:
    if score>=max:
        max=score
print(f"The max element is {max}")

# Gauss challenge
sum=0
for num in range(1,101):
    sum+=num
print(sum)

#Day5 Project - Pypassword_list Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Pypassword_list Generator!")
num_let=int(input("How many letters would you like?\n"))
num_sym=int(input("How many numbers would you like?\n"))
num_num=int(input("How many numbers would you like?\n"))
password_list=''
for c in range(0,num_let): 
    password_list+=random.choice(letters)
for s in range(0,num_sym):
    password_list+=random.choice(symbols)
for n in range(0,num_num):
    password_list+=random.choice(numbers)

print(password_list)

# Hard level - randomize the order of letters, numbers and symbols
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")
num_let=int(input("How many letters would you like?\n"))
num_sym=int(input("How many numbers would you like?\n"))
num_num=int(input("How many numbers would you like?\n"))
password_list=[]
for c in range(0,num_let): 
    password_list+=random.choice(letters)
for s in range(0,num_sym):
    password_list+=random.choice(symbols)
for n in range(0,num_num):
    password_list+=random.choice(numbers)
random.shuffle(password_list)
password=''
for char in password_list:
    password+=char
print(f"Your password generated is {password}")
    




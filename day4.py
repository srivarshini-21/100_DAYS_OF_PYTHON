# # Day4
# import random
# print(random.randint(1,7))
# print(random.random())
# print(random.uniform(2,10))

# rand_head_tail=random.randint(0,1)
# if rand_head_tail==0:
#     print("Heads")
# else:
#     print("Tails")

# # Lists
# states=["Karnataka","Tamil Nadu","Punjab","Gujarat"]
# print(states[0])
# states[2]="Kerala"
# print(states)
# states.append("Bihar")
# print(states)
# states.extend(["Rajastan","West Bengal","Andhra Pradesh"])
# print(states)

# # Who's gonna pay
# ppl=['Alice','Bob','Charlie','David','Emanuel']
# i=random.randint(0,4)
# print(f"Person paying the bill: {ppl[i]}")

# #Alt soln
# print(random.choice(ppl))
# # Acessing in nested lists
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][1])

# # Day4 Project
# rock="""
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """
# paper="""
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """
# scissors="""
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """
# game_img=[rock,paper,scissors]
# player=int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors\n"))
# if player>=3 or player<0:
#     print("Invalid input. You lose!")
# else:
#     print(game_img[player])    

# comp_choice=random.randint(0,2)
# print(f"Computer chose:\n {game_img[comp_choice]}")
# if player==comp_choice:
#     print("It's a draw!")
# elif player==0 and comp_choice==2:
#     print("You win!")
# elif player ==2 and comp_choice==0:
#     print("You lose!")
# elif player<comp_choice:
#     print("You lose!")
# elif player>comp_choice:
#     print("You win!")




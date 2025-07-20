# Day1
print("hello world\nHello world")
print("Hey"+" ruby") 
print("Hello " + input("Whats your name?") + "!")
username = input("Username:")
length= len(username)
print(length)
#Day1 project
print("Welcome to Band Name Generator")
city=input("Whats the name of the city you grew up in?")
pet=input("Whats the  name of your pet?")
print("Your band name could be " +city+" " +pet)

# Day2
print(type("hey"))
print(type(1234))
print(type(123.456))
print(type(False))
print(float(1234))
print(int(123.456))
print(str(1234.567))
print(bool("nope"))

print("Number of letters in your name is " + str(len(input("Whats your name?"))))

# Calculate BMI
height=1.65
weight = 84
bmi=weight/height**2
print(bmi)

# Day2 Project
print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill?"))
tip=int(input("How much would you like to tip? 10, 12 or 15?"))
people=int(input("How many people to split the bill?"))
ppbill=(((tip/100)*total_bill)+total_bill)/people
ppbill_ro=round(ppbill,2)
print(f"Each person should pay: ${ppbill_ro}")

# Day3
num=int(input("Enter a number:"))
if num % 2 ==0:
    print("The number is even")
else:
    print("The number is odd")

print("Welcome to rollercoaster!")
bill=0
h=int(input("Height: "))
if h>=120:
    print("You can ride")
    age = int(input("Age: "))
    if age <=12:
        bill=5
        print("Child - $5")
    elif age <=18:
        bill=7
        print("Youth - $7")
    elif age>=45 and age<=55:
        bill=0
        print("You get a free ride!")
    else:
        print("Adult - $12")
        bill = 12
    pic = input("Do you want pics? Type y for yes and n for no ")
    if pic == "y":
        bill+=3
    print(f"Please pay ${bill} ")

else:
    print("You can't ride")

# Pizza Price calci
print("Welcome to Pizzeria!")
bill=0
size = input("Which size pizza? S, M or L? ")
if size=="S":
    bill=15
elif size=="M":
    bill=20
elif size=="L":
    bill=25
pepparoni=input("Do you want pepparoni? Y or N: ")
if pepparoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
cheese=input("Do you want extra cheese? Y or N: ")
if cheese=="Y":
    bill+=1

print(f"Your final bill is ${bill}")

# Day3 Project - Treasure Island
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure")
print("You are at a cross road. Where do you want to go?")
op1=input("Type 'left' or 'right'\n")
if op1=="left":
    print("You have come to a lake. There is an island in the middle of the lake.")
    op2=input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if op2=="wait":
        print("You arrive at the island unharmed. There are 3 doors. One red, one yellow and one blue. ")
        op3=input("Which color do you choose?\n")
        if op3=="red":
            print("It's a room full of fire. Game Over.")
        elif op3=="yellow":
            print("You found the treasure! You win!")
        elif op3=="blue":
            print("You enter a room full of beasts. Game Over.")
    elif op2=="swim":
        print("You get attacked by an angry trout. Game Over.")
elif op1=="right":
    print("You fell into a hole. Game Over.")

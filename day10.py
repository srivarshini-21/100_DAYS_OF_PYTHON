# # Functions with Outputs
# def name_merge(fname,lname):
#     """This is a docstring. Displays documentation for this function"""
#     formatted_f=fname.title()
#     formatted_l=lname.title()
#     return f"{formatted_f}{formatted_l}"
# merger=name_merge("RUBy ", "JoSEpH")
# print(merger)

# Day 10 Project - Calculator
logo=r'''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|'''
art=r'''
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                             '''
def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    if n2 == 0:
        print("Division by zero not allowed")
    else:
        return n1 / n2
    
operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def calculator():
    print(logo,art)
    should_continue = True
    n1=int(input("What's the first number? : "))
    while should_continue:
        for symbol in operations:
            print(symbol)
        op=input("Pick an operation: \n")

        n2=int(input("What's the next number? : "))
        ans=operations[op](n1,n2)
        print(f"{n1} {op} {n2} = {ans}")

        choice = input(f"Type 'yes' if you want to continue with {ans} or type 'no' to start new calculation. \n")

        if choice=="yes":
            n1=ans
        else:
            should_continue=False
            calculator()
calculator()
        



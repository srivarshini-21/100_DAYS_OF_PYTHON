# Day 15 - Coffee Machine project
logo=r'''

                       .
                        `:.
                          `:.
                  .:'     ,::
                 .:'      ;:'
                 ::      ;:'
                  :    .:'
                   `.  :.
          _________________________
         : _ _ _ _ _ _ _ _ _ _ _ _ :
     ,---:".".".".".".".".".".".".":
    : ,'"`::.:.:.:.:.:.:.:.:.:.:.::'
    `.`.  `:-===-===-===-===-===-:'
      `.`-._:                   :
        `-.__`.               ,' 
    ,--------`"`-------------'--------.
     `"--.__                   __.--"'
            `""-------------""'

'''
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]: # Check if there is enough water/coffee for making a latte against the resources present
            print(f"Sorry there is not enough {item} to make your coffee.")
            return False # Ingredients not enough
    return True # Else: ingredients enough to prepare

def process_coins():
    """Returns total calculated amount from the coins inserted."""
    print("Please insert coins.\n")
    total=int(input("How many quarters?: ")) * 0.25 # 1 quarter = 0.25 cents
    total+=int(input("How many dimes?: ")) * 0.1 # 1 dime = 0.1 centa
    total+=int(input("How many nickles?: ")) * 0.05 # 1 nickle = 0.05 cents
    total+=int(input("How many pennies?: ")) * 0.01 # 1 penny = 0.01 cents
    return total
    # Declare once and update with the values each time

def is_transaction_success(money_received, drink_cost):
    """Returns true if payment is accepted and False if it's insufficient"""
    if money_received > drink_cost:
        global profit # Optional - when the ide doesn't let you modify global var in local scope 
        profit+=drink_cost
        change=round(money_received-drink_cost,2) # Rounds off the change to 2 decimal places
        print(f"Here's your change: ${change}")
        return True
    else:
        print("Sorry, insufficient funds. Money refunded.")
        return False
    
def make_coffee(drink_name, order_ingredients):
    """Deducts the ingredients used  from the resources"""
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here's your drink, {drink_name}☕. Enjoy!")

print(logo)
print("Welcome to the coffee machine!")
is_on=True
while is_on:
    choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink=MENU[choice] # To access the drink chosen from MENU
        if is_resource_sufficient(drink['ingredients']):
            payment=process_coins()
            if is_transaction_success(payment,drink['cost']):
                make_coffee(choice,drink["ingredients"])


    
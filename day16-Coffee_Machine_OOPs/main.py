# All the other files in this folder were pre-written 
# This Project was to understand how OOPs works and how we can code the same program we did yesterday using OOPs
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()
is_on=True

while is_on:
    options = menu.get_items()
    choice=input(f"What would you like? {options}: ").lower()
    if choice=='off':
        is_on=False
    elif choice=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



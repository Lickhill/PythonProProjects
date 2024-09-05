from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys


if (
    input("Do you want the report of resources and the menu then type 'report':")
    == "report"
):
    CoffeeMaker().report()
    print()
    MoneyMachine().report()
    print(Menu().get_items())

order = input("What would you like to have type it:")
drink = Menu().find_drink(order)
print(f"You order is a {drink}")

if CoffeeMaker().is_resource_sufficient(drink) == False:
    print("We do not have enough resources")
    sys.exit()

print(f"The cost of your drink is {drink.cost}")
if MoneyMachine().make_payment(drink.cost) == False:
    print("Not enough money")
    sys.exit()

CoffeeMaker().make_coffee(drink)

MoneyMachine().report()

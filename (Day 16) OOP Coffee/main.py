from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
options = menu.get_items()
coffeemaker = CoffeeMaker()
money_stuff = MoneyMachine()
is_on = True

while is_on:
    ordered_drink = input(f"What drink do you want ({options}): ")
    if ordered_drink == "report":
        coffeemaker.report()
        money_stuff.report()
    elif ordered_drink == "off":
        is_on = False
    elif menu.find_drink(ordered_drink):
        drink = menu.find_drink(ordered_drink)
        if coffeemaker.is_resource_sufficient(drink) and money_stuff.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)




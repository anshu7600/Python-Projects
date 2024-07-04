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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money_profit = 0
is_coffee_machine_on = True


def check_sufficient_resources(coffee_name):
    drink_ingredients = MENU[coffee_name]["ingredients"]
    for item in MENU[coffee_name]["ingredients"]:
        if resources[item] > drink_ingredients[item]:
            pass
        else:
            return print("Sorry there is not enough " + item)
    return True


def ask_money():
    quarters = int(input("How many Quarters: ")) * 0.25
    dimes = int(input("How many Dimes: ")) * 0.1
    nickles = int(input("How many Nickles: ")) * 0.05
    pennies = int(input("How many Pennies: ")) * 0.01
    return quarters + round(dimes, 2) + round(nickles, 2) + pennies


def check_money(money, coffe_name_ordered):
    global money_profit
    drink_cost = MENU[coffe_name_ordered]["cost"]
    if drink_cost < money:
        print(f"Here is ${float(money) - drink_cost} dollars in change.")
        money_profit += drink_cost
        return True
    elif drink_cost == money:
        money_profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name):
    for item in MENU[drink_name]["ingredients"]:
        resources[item] -= MENU[drink_name]["ingredients"][item]
    return print(f"Here is your {drink_name}. Have a Great Day!")


while is_coffee_machine_on:
    coffee_name_input = input("What would you like? (Espresso/Latte/Cappuccino): ")
    if coffee_name_input.lower() == "off":
        is_coffee_machine_on = False
    elif coffee_name_input.lower() == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${money_profit}")
    elif check_sufficient_resources(coffee_name_input):
        if check_money(ask_money(), coffee_name_input):
            make_coffee(coffee_name_input)
    else:
        check_sufficient_resources(coffee_name_input)
        continue

print("Coffe Machine Turned OFF")

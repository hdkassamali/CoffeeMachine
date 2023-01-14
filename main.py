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
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0,
}


def check_resources(drink):
    if drink != "espresso":
        if resources["Milk"] < MENU[drink]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return False
    if resources["Water"] < MENU[drink]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    elif resources["Coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


def process_coins():
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    return quarters + dimes + nickles + pennies


def check_transaction(paid, drink):
    change = 0
    if paid < MENU[drink]["cost"]:
        return "Sorry that's not enough money. Money refunded."
    else:
        resources["Money"] += MENU[drink]["cost"]
        change = round(paid - MENU[drink]["cost"], 2)
        return f"Here is ${change} in change."


def make_coffee(drink):
    if drink != "espresso":
         resources["Milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["Water"] -= MENU[drink]["ingredients"]["water"]
    resources["Coffee"] -= MENU[drink]["ingredients"]["coffee"]
    return f"Here is your {drink} ☕️ Enjoy!"


machine_is_on = True
while machine_is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        machine_is_on = False
    elif order == "report":
        print(f"Water: {resources['Water']}ml")
        print(f"Milk: {resources['Milk']}ml")
        print(f"Coffee: {resources['Coffee']}g")
        print(f"Money: ${resources['Money']}")
    elif order == "espresso" or "latte" or "cappuccino":
        enough_resources = check_resources(order)
        if enough_resources:
            print("Please insert coins.")
            total_paid = process_coins()
            transaction = check_transaction(total_paid, order)
            print(transaction)
            if total_paid >= MENU[order]["cost"]:
                give_drink = make_coffee(order)
                print(give_drink)





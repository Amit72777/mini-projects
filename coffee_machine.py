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
# TODO 4 : Check resource sufficient


def check_resource(order_ingredient):
    """Return True when order can be made, False if ingredient are insufficient """
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coin():
    """Return the total calculated from coins inserted."""
    print("please insert coins.")
    total = int(input("How many quarters?:")) * 0.25
    total += int(input("How many dimes:?")) * 0.1
    total += int(input("How many nickels?:")) * 0.05
    total += int(input("How many pennies?:")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """return True when payment is accepted , or money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"her is ${change} is change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} \n")


is_on = True

while is_on:
    choice = input("What would you line ? (espresso / latte / cappuccino):")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water : {resources['water']}")
        print(f"Milk : {resources['milk']}")
        print(f"Coffee : {resources['coffee']}")
        print(f"Money : {profit}")
    else:
        drink = MENU[choice]
        print(drink)
        if check_resource(drink['ingredients']):
            payment = process_coin()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])

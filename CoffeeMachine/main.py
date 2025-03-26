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
profit = 0

def is_resource_sufficient(order_ingredients):
    """checks the available resources left in the machine"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return  False
    return True

def process_coins():
    """returns the total calculated coins inserted into the machine"""
    print("Please insert coins. ")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return  total
dispense_on = True
while dispense_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        dispense_on = False
    elif choice == "report":
        print(f"Coffee:{resources['coffee']}g")
        print(f"water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Money:${profit}")
    else:
        drink = MENU[choice]
        is_resource_sufficient(drink['ingredients'])

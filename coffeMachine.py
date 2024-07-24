# GLOBAL VARIABLES BELOW
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


# FUNCTIONS BELOW
def coffee_art():
    """It shows The Coffee Project Machine its own menu."""
    print('''\033[33m
         )))
        (((
      +-----+
      |     |] - WELCOME TO THE COFFEE MACHINE!
      `-----' 

      ------ MENU ------ 
      Espresso ($1.50)
      Latte ($2.50)
      Cappuccino ($3.00)
      ------------------

      PS: Type "report" at any moment
      to check our resources available.
      Type "off" to log out from the machine.\033[m
    ''')


def show_report():
    """It shows the resources report of the Coffee Machine."""
    print('\033[34mHere is our current resources.\033[m')
    for k, v in resources.items():
        print(f'\033[34m{k.title()}: {v}ml\033[m')
    print(f'\033[34mMoney: ${money}\033[m')


def check_resources(user_choice):
    """It checks if resources are sufficient (True) or not (False)"""
    if MENU[user_choice]["ingredients"]["water"] > resources["water"]:
        print(f'\033[31mSorry. There is not sufficient water for the beverage.\n'
              f'We currently have {resources["water"]}ml of water in storage.\033[m')
        return False
    elif MENU[user_choice]["ingredients"]["milk"] > resources["milk"]:
        print(f'\033[31mSorry. There is not sufficient milk for the beverage. \n'
              f'We currently have {resources["milk"]}ml of milk in storage.\033[m')
        return False
    elif MENU[user_choice]["ingredients"]["coffee"] > resources["coffee"]:
        print(f'\033[31mSorry. There is not sufficient coffee for the beverage. \n'
              f'We currently have {resources["coffee"]}ml of coffee in storage.\033[m')
        return False
    else:
        print(f'Great choice! Allow us to charge you now.')
        return True


def charge_user(user_choice):
    """It charges the user to insert coins for the required beverage."""
    print('''\033[33m
    We accept the following coins:
    Quarters ($0.25), dimes ($0.10)
    nickles ($0.05), pennies ($0.01)\033[m
    ''')
    quarters = int(input('How many quarters will you insert? Please: '))
    dimes = int(input('How many dimes will you insert? Please: '))
    nickles = int(input('How many nickles will you insert? Please: '))
    pennies = int(input('How many pennies will you insert? Please: '))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    print(f'You provided: ${total:.2f}')
    if total > MENU[user_choice]["cost"]:
        change = total - MENU[user_choice]["cost"]
        print(f'Your change: ${change:.2f}\nThank you! We will make your beverage now.')
        total -= change
        return total
    else:
        print(f'Sorry. The money is not sufficient for the required beverage.\nMoney refunded.')


def update_storage(user_choice):
    """It updates the Coffee Machine resources after a beverage is ordered."""
    resources["water"] = resources["water"] - MENU[user_choice]["ingredients"]["water"]
    resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]
    resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
    return resources


# MAIN CODE BELOW
while True:
    coffee_art()
    while True:
        user_choice = str(input('What would you like? (espresso/latte/cappuccino): ')).strip().lower()
        if user_choice == "off":
            print('\033[31m<<THE END>>\033[m')
            exit()
        elif user_choice == "report":
            show_report()
        elif user_choice not in MENU:
            print('\033[31mError. Please choose an available option.\033[m')
        else:
            print(f'You chose "{user_choice}" and it costs ${MENU[user_choice]["cost"]:.2f}')
            if check_resources(user_choice) is True:
                money += charge_user(user_choice)
                resources = update_storage(user_choice)
                break
    print(f'''
         )))
        (((
      +-----+
      |     |] - Here's your {user_choice}. Enjoy! :)
      `-----'
    ''')

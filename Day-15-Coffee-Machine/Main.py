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
money = 0
user_choice = str(input("What would you like? ( espresso / latte / cappuccino ) :")).lower()
if user_choice == "report":
    #The report Section
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money : {money}$")

quarters = int(input("Please Enter quarters : ")) * 0.25
dimes = int(input("Please Enter dimes : ")) * 0.10
nickles = int(input("Please Enter nickles : ")) * 0.05
pennies = int(input("Please Enter pennies : ")) * 0.01
total_coins = quarters+ dimes + nickles + pennies



# TODO check resources sufficient
# TODO process coins
# TODO check transaction successful?
# TODO make the coffee

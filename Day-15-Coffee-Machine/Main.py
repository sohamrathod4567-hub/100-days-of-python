import art
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
machine_on = True
def make_coffee(drink):
    """This function will deduct the required ingredients from the resources"""
    for i in drink["ingredients"]:
        resources[i] -=  drink["ingredients"][i]

def coffee_money(cost,choice,sel_drink):
    """This function will take the coins from the user and check if it is enough to make the coffee"""
    quarters = int(input("Please Enter quarters : ")) * 0.25
    dimes = int(input("Please Enter dimes : ")) * 0.10          # This is the logic where the user will enter the coins and the total will be calculated and checked if it is enough to make the coffee
    nickles = int(input("Please Enter nickles : ")) * 0.05
    pennies = int(input("Please Enter pennies : ")) * 0.01
    total_coins = quarters + dimes + nickles + pennies
    print(f"Your total is: {total_coins:.2f}$ ")
    if total_coins < cost:
        print(f"Sorry that is not enough for the {choice} Here is your refund")
    else:
        if total_coins > cost:
            change = total_coins - cost
            print(f"Here is you change : {change:.2f}$")
        print(f"Enjoy your {choice}")
        global money
        money +=  cost
        make_coffee(sel_drink)


def report():
    """This function will print the report of the resources and money"""
    #The report Section
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money : ${money}")
while machine_on:
    """This is the main loop of the coffee machine program. It will keep running until the user turns off the machine."""
    print(art.logo)
    user_choice = str(input("What would you like? ( espresso / latte / cappuccino ) :")).lower()

    if user_choice == "report":
        report()
        continue
    if user_choice == "off":
        machine_on = False
        print("Thank You for choosing us")
        break
    if user_choice not in MENU:
        print("Invalid Choice")
        continue
    else:
        selected_drink = MENU[user_choice]
    can_make_coffee = True
    for ingredient in selected_drink["ingredients"]:
        if selected_drink["ingredients"][ingredient] > resources[ingredient]:
            print(f"You do not have enough {ingredient} Sorry!!")
            can_make_coffee = False
            break
    if can_make_coffee:
        coffee_money(selected_drink["cost"],user_choice,selected_drink)
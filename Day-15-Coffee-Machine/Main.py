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
    for i in drink["ingredients"]:
        resources[i] -=  drink["ingredients"][i]

def coffee_money(cost,choice,sel_drink):
    quarters = int(input("Please Enter quarters : ")) * 0.25
    dimes = int(input("Please Enter dimes : ")) * 0.10
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
    #The report Section
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money : ${money}")
while machine_on:

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
    # print(selected_drink["ingredients"])
    # print(selected_drink)
    can_make_coffee = True
    for ingredient in selected_drink["ingredients"]:
        # print(ingredient)
       # print(resources[ingredient]) # Available
       #  print(selected_drink["ingredients"][ingredient]) # Required
        if selected_drink["ingredients"][ingredient] > resources[ingredient]:
            print(f"You do not have enough {ingredient} Sorry!!")
            can_make_coffee = False
            break

    if can_make_coffee:
        coffee_money(selected_drink["cost"],user_choice,selected_drink)

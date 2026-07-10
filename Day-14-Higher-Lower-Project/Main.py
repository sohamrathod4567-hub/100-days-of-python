import random
import art
import game_data
def format_data(account):
    """Formate the account data into printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc} , from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take a use's guess and follower count of a and b and returns if they get it right"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
score = 0
game_should_continue =True

account_b = random.choice(game_data.data)
while game_should_continue :
    account_a = account_b
    account_b = random.choice(game_data.data)
    if account_a == account_b:
        account_b = random.choice(game_data.data)

    print(art.logo)
    print(f"Compare A : {format_data(account_a)}")
    print(art.vs)
    print(f" Against B : {format_data(account_b)}")

    guess =  str(input("Who has more Instagram Followers ? A / B ")).lower()
    print("\n " *20 )
    print(art.logo)

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        print("You are Right!")
        score += 1
        print(f"Your Score is : {score}")
    else:
        print("Wrong Answer!")
        print(f"Your Final Score is {score}")
        game_should_continue = False

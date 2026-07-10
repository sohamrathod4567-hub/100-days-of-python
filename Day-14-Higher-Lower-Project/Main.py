import random
import art
import game_data
account_a = random.choice(game_data.data)
account_b = random.choice(game_data.data)
        # The details for the first person
name_a = account_a["name"]
followers_a = account_a["follower_count"]
description_a = account_a["description"]
country_a = account_a["country"]
        # The details for the second person
name_b = account_b["name"]
followers_b = account_b["follower_count"]
description_b = account_b["description"]
country_b = account_b["country"]
print(name_a)
print(art.vs)
print(name_b)

def followers_checker(a, b):
    if a > b:
        return "a"
    else:
        return "b"

result_followers = followers_checker(followers_a,followers_b)

print(result_followers)

def user_choice(which):
    if which == result_followers :
        if result_followers == "a":
            print(f"You are Right {name_a} has more followers {followers_a}")
        else:
            print(f"You are Right {name_b} has more followers {followers_b}")
    else:
        print("You are wrong")

user_choice(which = str(input("Who has more Instagram Followers ? A / B ")).lower())

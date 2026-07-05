import art
print(art.logo)
details = {}
finish = True
while finish:

    name = str(input("What is your name?\n ")).lower()
    bid = int(input("How much do you bid?\n $"))
    details[name] =bid
    # print(details)
    Continue = str(input("Do you want to continue? [y/n]")).lower()
    if Continue =="n":
        finish = False
        compare = max(details, key=details.get)
        print(f"The winner is {compare} with a bid of ${details[compare]}")
    else:
        print("\n" * 200)
        print(art.logo)
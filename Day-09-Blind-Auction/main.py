import art
print(art.logo)
details = {} #declare a dictionary to store the name and bid amount of each participant
finish = True
while finish:

    name = str(input("What is your name?\n ")).lower()
    bid = int(input("How much do you bid?\n $"))
    details[name] =bid #this is a dictionary that stores the name and bid amount of each participant
    # print(details)
    Continue = str(input("Do you want to continue? [y/n]")).lower()
    if Continue =="n":
        finish = False
        compare = max(details, key=details.get) #this line of code finds the key (name) with the maximum value (bid) in the details dictionary
        print(f"The winner is {compare} with a bid of ${details[compare]}")
    else:
        print("\n" * 200) #to print 200 new lines to clear the console screen for the next participant
        print(art.logo)
import random
import art

print(art.logo)
number = random.randint(1,100)
print("Welcome to the Number Guessing Game")
hard_mode = str(input("Choose difficulty: Easy (e) or Hard (h): ")).lower()
if hard_mode in ("e" , "easy" ):
    life = 10
else:
    life = 5
print(f"You now have : {life} life left")
while True:
    user_guess = int(input("Guess a number between 1 and 100: "))
    if number ==user_guess:
            print(f"You guessed the number right it was {number}")
            print("You win")
            break
    elif number > user_guess:
            print("That is Too low")
    elif number < user_guess:
            print("That is Too high")
    life -= 1
    print(f"You have : {life} life left")
    if life == 0:
        print("You lose")
        print(f"\n The number was {number} Better Luck next time\n ")
        break
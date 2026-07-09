import random
import art
def high_low ():
    """This Function is a game where the user has to guess a number between 1 and 100. The user can choose the difficulty level, which determines the number of attempts they have to guess the correct number."""
    print(art.logo)
    number = random.randint(1,100) #This is where the system generates a random number between 1 and 100 for the user to guess.
    print("Welcome to the Number Guessing Game")
    hard_mode = str(input("Choose difficulty: Easy (e) or Hard (h): ")).lower() #Game mode Selection
    if hard_mode in ("e" , "easy" ): #Handaling if the user chooses easy instead of e
        life = 10
    else:
        life = 5
    print(f"You now have : {life} life left")
    while True: #The main loop where the magic happens. The user is prompted to guess a number between 1 and 100, and the system checks if the guess is correct, too high, or too low. The user has a limited number of attempts based on the difficulty level they chose.
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

again = "y"
while again == "y": #This loop allows the user to play the game again if they choose to do so. After each game, the user is prompted to play again or exit the game.
    high_low()
    again = str(input("Do you want to play again? y/n")).lower()
    print("\n" * 200)
print("Thank you for playing")




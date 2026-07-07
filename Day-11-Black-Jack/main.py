import random
import art
#The Deck of cards, Here 11 is ace which will change according to the total of the user Which is covered later in the code
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(weight):
    """This Function is used to give cards to both the user and the dealer. """
    return random.choices(cards,k = weight) # here I have written this in  way

def calculate_score(got_cards):
    """This function is used to calculate the score of the user and the dealer. """
    if len(got_cards) == 2 and sum(got_cards) == 21: # If BlackJack is there then return 0 which is used to check in the main function
        return 0
    # If the total is greater than 21 and there is an ace in the cards then change the value of ace from 11 to 1
    if sum(got_cards) > 21 and 11 in got_cards:
        got_cards.remove(11)
        got_cards.append(1)
    return sum(got_cards)
def compare(user_score,dealer_score):
    """This function is used to compare the score of the user and the dealer and print the result. """
    if user_score > 21:
        print("User Busted")
    elif dealer_score > 21:
        print("Dealer Busted")
    elif user_score == dealer_score:
        print("IT is a Draw")
    elif user_score == 0 :
        print("That is BlackJack for the user")
        print("User Wins!!")
    elif dealer_score == 0 :
        print("That is a black jack for the dealer ")
        print("Dealer wins")
    elif user_score > dealer_score:
        print("User Wins!!")
    elif dealer_score > user_score:
        print("Dealer Wins!!")
def black_jack():
    """This is the main function which is used to play the game. """
    user_cards = []
    dealer_cards = []
    on = True
    # print(user_cards)
    # print(dealer_cards)

    user_cards.extend(deal_card(2))
    dealer_cards.extend(deal_card(2))
    print(f"user_cards are : {user_cards}")
    print(f"Total is {calculate_score(user_cards)}")
    print(f"dealer_cards are : {dealer_cards}")
    print(f"Total is {calculate_score(dealer_cards)}")
    while on:
        user_total = calculate_score(user_cards)
        dealer_total = calculate_score(dealer_cards)
        if user_total == 0 or dealer_total == 0 :
            compare(user_total,dealer_total)
            break
        if user_total> 21:
            compare(user_total,dealer_total)
            break
        if dealer_total> 21:
            compare(user_total,dealer_total)
            break
        more_card = str(input("Do you want to Draw a card? (y/n): ")).lower()
        if more_card == "y":
            user_cards.extend(deal_card(1))
            print("User's cards are : ", user_cards)
            print(f"Total is {calculate_score(user_cards)}")
            user_total = calculate_score(user_cards)

        if more_card == "n":
            while dealer_total < 17:
                dealer_cards.extend(deal_card(1))
                print("Dealer's cards are : ", dealer_cards)
                print(f"Total is {calculate_score(dealer_cards)}")
                dealer_total = calculate_score(dealer_cards)
            else:
                compare(user_total,dealer_total)
                on = False
#This is the main loop which is used to restart the game if the user wants to play again.
restart = "y"
while restart == "y":
    print("\n"*200)

    print(art.logo)
    black_jack()

    restart = input("\nDo you want to play another game? (y/n): ").lower()

print("Thanks for playing!")
import random
import hangman_words
import hangman_art
stages = hangman_art.stages
word_list = hangman_words.word_list

lives = 6


print(hangman_art.logo)
chosen_word = random.choice(word_list)
# print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:


    print(f"**************************** {lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()


    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print(f"You Have already typed The word {guess}")


    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        print(f"{guess} is incorrect")
        print("You lose a life")
        lives -= 1

        if lives == 0:
            game_over = True


            print(f"***********************YOU LOSE**********************")
            print(f"The correct word was ==========>     {chosen_word}")

    if "_" not in display:
        print("****************************YOU WIN****************************")
        game_over = True


    print(stages[lives])

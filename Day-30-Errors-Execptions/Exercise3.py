import pandas


nato = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_pairs = {row.letter:row.code for (index, row) in nato.iterrows()}

# print(nato_pairs)
def generate_phonetic():
    user_input = input("What is your name?").strip().upper()
    try:
        phonetics = [nato_pairs[name] for name in user_input]
    except KeyError:
        print("Invalid input. Please try again.")
        generate_phonetic()
    else:
        print(phonetics)
generate_phonetic()
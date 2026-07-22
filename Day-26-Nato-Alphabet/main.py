import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

user_input = input("What is your name?").strip().upper()

nato = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_pairs = {row.letter:row.code for (index, row) in nato.iterrows()}

print(nato_pairs)

phonetics = [nato_pairs[name] for name in user_input]
print(phonetics)



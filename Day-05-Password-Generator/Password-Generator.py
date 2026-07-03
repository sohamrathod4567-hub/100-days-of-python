import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
a = []
b = []
c = []
for l in range(nr_letters) :
    a+= random.choice(letters)              #This is a code for  the normal password generator

for o in range(nr_symbols) :
    b+= random.choice(symbols)

for p in range(nr_numbers) :
    c+= random.choice(numbers)

# here is our normal password
password =  a + b + c
print(f"Your Normal password is :{password}")



# This step is for shuffled password
random.shuffle(password)  #this function does not return anything
final_pass = ""
print(f"Your Shuffled Password is :{final_pass.join(password)}")




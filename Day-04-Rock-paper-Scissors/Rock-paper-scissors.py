import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
Selection = [rock,paper,scissors]
User = input("Rock: 0\npaper: 1\nScissors:2 ")
if User == "0" :
    print("\nRock" +  rock)
if User == "1" :
    print("\nPaper" + paper)
if User == "2" :
    print("\nScissors" + scissors)

print("Computer Choose: ")
random_index = random.randint(0, 2)
print(Selection[random_index])

if random_index == 0 and User == "0":
    print("Try Again")
if random_index == 1 and User == "0":
    print("Computer Wins")
if random_index == 2 and User == "0":
    print("You win")
if random_index == 0 and User == "1":
    print("YOu win")
if random_index == 0 and User == "2":
    print("Computer Win")
if random_index == 1 and User == "1":
    print("Try Again")
if random_index == 2 and User == "2":
    print("Try Again")
if random_index == 1 and User == "2":
    print("YOu win")
if random_index == 2 and User == "1":
    print("Computer won")

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"])
#
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")
from numpy.random.mtrand import weibull

height = float(input("Enter your height : "))
weight = int(input("Enter your weight : "))


if height > 3 :
    raise ValueError("Your height is too high")
bmi = weight/ height ** 2


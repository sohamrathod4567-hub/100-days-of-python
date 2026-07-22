list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(number) for number in list_of_strings]
result =[ even for even in numbers if even %2 == 0]
print(result)
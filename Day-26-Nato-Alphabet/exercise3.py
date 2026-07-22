with open("file1.txt") as file:
    file_1 = [int(line) for line in file.readlines()]

with open("file2.txt") as file:
    file_2 = [int(line) for line in file.readlines()]

print(file_1)
print(file_2)

result =[num for num in file_1 if num in file_2 ]

print(result)
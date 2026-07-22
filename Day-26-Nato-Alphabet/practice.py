import random
# name = "soham"
# new_list = [letter for letter in name] # this is how you do the list comprehension
# print(new_list)
#
# new_numbers = [n*2 for n in range(1,5)]
# print(new_numbers)
# print(new_numbers)
#
# short_names = [name for name in names if len(name) < 5 ]
# print(short_names)
#
# Cap_names = [name.upper() for name in names if len(name) > 5 ]
# print(Cap_names)

names = ["Alex", "fred","caroline"," simon", "wilson", "lo sinto"]

students_scores = {
    student:random.randint(1,100) for student in names
}
passed_students = {student : score for (student,score) in students_scores.items() if score > 60 }
print(students_scores)
print(passed_students)
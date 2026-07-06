import art
print(art.logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
Restart = True
Calculator = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
number1 = int(input("Enter the first number: "))
operation = input("Enter the operation +, -, *, / : ")
number2 = int(input("Enter the second number: "))
while Restart:
    result = 0
    if operation =="+":
        result = Calculator["+"](number1,number2)
        print(result)
    if operation =="-":
        result =  Calculator["-"](number1,number2)
        print(result)
    if operation =="*":
        result =  Calculator["*"](number1,number2)
        print(result)
    if operation =="/":
        result =  Calculator["/"](number1,number2)
        print(result)
    cont = str(input("Do you want to continue (y/n)? "))
    if cont == "y":
        number1 = result
        print(f"Your First number is {result}")
        operation = input("Enter the operation +, -, *, / : ")
        number2 = int(input("Enter the second number: "))
    if cont == "n":
        print("\n" * 169)
        print(art.logo)
        number1 = int(input("Enter the first number: "))
        operation = input("Enter the operation +, -, *, / : ")
        number2 = int(input("Enter the second number: "))

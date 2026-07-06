import art
print(art.logo)

# Basic math operations used by the calculator.
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

Restart = True

# This dictionary lets us call a function based on the chosen symbol.
Calculator = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

# Take the first calculation input before entering the loop.
number1 = float(input("Enter the first number: "))
operation = input("Enter the operation +, -, *, / : ")
number2 = float(input("Enter the second number: "))
while Restart:
    result = 0
    # Check which operation the user selected and run that function.
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

    # Ask whether to continue with the result or start over.
    cont = str(input("Do you want to continue (y/n)? "))
    if cont == "y":
        number1 = result
        print(f"Your First number is {result}")
        operation = input("Enter the operation +, -, *, / : ")
        number2 = float(input("Enter the second number: "))
    if cont == "n":
        # Clear the screen effect and restart with fresh inputs.
        print("\n" * 169)
        print(art.logo)
        number1 = float(input("Enter the first number: "))
        operation = input("Enter the operation +, -, *, / : ")
        number2 = float(input("Enter the second number: "))

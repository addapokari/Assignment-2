# calculator functions
# 1.add
from matplotlib.pylab import choice


def add(x, y):
    return x + y

# 2.subtract
def subtract(x, y):
    return x - y

# 3.multiply
def multiply(x, y):
    return x * y

# 4.divide
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

# 5.modulus
def modulus(x, y):
    if y == 0:
        return "Error: Modulus by zero is not allowed."
    return x % y

# 6.power
def power(x, y):
    return x ** y
# 7.square root
def square_root(x): 
    if x < 0:
        return "Error: Square root of a negative number is not defined."
    return x ** 0.5
# 8.percentage
def percentage(part, whole):
    if whole == 0:
        return "Error: Percentage with a whole of zero is not defined."
    return (part / whole) * 100 
# 9. calculator function
def calculator():       

    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Square Root")
        print("8. Percentage") 
        print("9. Exit") 

        choice = input("Enter your choice (1-9): ")

        if choice == '9':
            print("Exiting the calculator. Goodbye!")
            break
        if choice == '7':
            num = float(input("Enter a number: "))
            print(f"Square root of {num} is: {square_root(num)}")
        if choice == '8':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"Percentage of {num1} with respect to {num2} is: {percentage(num1, num2)}")
        if choice in ['1', '2', '3', '4', '5', '6']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} % {num2} = {modulus(num1, num2)}")
            elif choice == '6':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
            elif choice == '7':
                print(f"{num1} square root is: {square_root(num1)}")    
            elif choice == '8':
                print(f"{num1} percentage of {num2} is: {percentage(num1, num2)}")
        else:
            print("Invalid choice! Please enter a number between 1 and 9.")
            # run the calculator
calculator()


# Factorial Calculator
# this calculate factorial of a number using a loop 
number = int(input("Enter a number to calculate its factorial: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("0! = 1")
else:
    factorial = 1
    print(f"{number}! = ", end="")
    for i in range(number, 0, -1):
        print(f"{i} ", end="")
        if i != 1:
            print("* ", end="")
        factorial *= i
    print(f"= {factorial}")


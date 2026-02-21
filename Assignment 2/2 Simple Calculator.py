# Simple CalculatorProgram

# Take user input for two numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Take user input for the operation

addistion= num1 + num2
subtraction= num1 - num2    
multiplication= num1 * num2
division= num1 / num2
modulus= num1 % num2
exponentiation= num1 ** num2
# Perform the selected operation and display the result

print(f"Addition: {num1} + {num2} = {addistion}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")        
print(f"Modulus: {num1} % {num2} = {modulus}")
print(f"Exponentiation: {num1} ** {num2} = {exponentiation}")
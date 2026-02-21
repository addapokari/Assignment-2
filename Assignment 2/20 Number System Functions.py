# Number System Functions
# create the following mathaematical functions:
# 1. factorial(n) - return n!
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# 2. check prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
# 3. fibonacci(n)
def fibonacci(n):
    if n <= 0:
        return "invalid input"
    elif n == 1:
        return [0]
    elif n == 2:
        return  1
    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
# 4. sum of digits
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))
# 5. reverse a number
def reverse_number(n):
    sign = -1 if n < 0 else 1
    reversed_num = int(str(abs(n))[::-1])
    return sign * reversed_num
# 6. check armstrong number
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == n
# 7. check GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)
# 8. check LCM
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
# 9. check perfect number
def is_perfect(n):
    if n < 1:
        return False
    total = 1
    for i in range(2, int (n ** 0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:  # Avoid double counting for perfect squares
                total += n // i
    return total == n
# 10. Menu function
def number_system_menu():
    while True:
        print("\nNumber System Functions Menu:")
        print("1. Factorial")
        print("2. Check Prime Number")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse a Number")
        print("6. Check Armstrong Number")
        print("7. GCD")
        print("8. LCM")
        print("9. Check Perfect Number")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == '10':
            print("Exiting the menu. Goodbye!")
            break
        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            n= int(input("Enter a number: "))
            if choice == '1':
                print(f"Factorial of {n} is: {factorial(n)}") 
            elif choice == '2':
                print(f"{n} is a prime number: {is_prime(n)}")
            elif choice == '3':
                print(f"Fibonacci of {n} is: {fibonacci(n)}")
            elif choice == '4':
                print(f"Sum of digits of {n} is: {sum_of_digits(n)}")
            elif choice == '5':
                print(f"Reversed number of {n} is: {reverse_number(n)}")
            elif choice == '6':
                print(f"{n} is an Armstrong number: {is_armstrong(n)}")
            elif choice == '7':
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print(f"GCD of {a} and {b} is: {gcd(a, b)}")
            elif choice == '8':
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print(f"LCM of {a} and {b} is: {lcm(a, b)}")
            elif choice == '9':
                print(f"{n} is a perfect number: {is_perfect(n)}")
            else:
                print("Invalid choice! Please enter a number between 1 and 10.")
number_system_menu()    
    
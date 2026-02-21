# Generator for Multiplication Tables
# Get input from the user for the number and the range of the multiplication table
number = int(input("Enter the number : "))
end_range = int(input("Enter the range (end): "))
# Generate and print the multiplication table
print(f" ===MULTIPLICATION TABLE GENERATOR===  ")
print(f"\nMultiplication Table for {number} up to {end_range}:")
for i in range(1, end_range + 1):
    result = number * i
    print(f"{number} x {i} = {result}")


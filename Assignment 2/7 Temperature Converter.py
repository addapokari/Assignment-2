# Temperature Converter Program
# Create a temprature converter with a menu-based system supporting the following conversions:
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# 3. Celsius to Kelvin
# 4. Kelvin to Celsius
# 5. Fahrenheit to Kelvin
# 6. Kelvin to Fahrenheit
# 7. Exit

while True:
    print("\n=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

    elif choice == '3':
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius + 273.15
        print(f"{celsius}°C is equal to {kelvin:.2f}K")

    elif choice == '4':
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin - 273.15
        print(f"{kelvin}K is equal to {celsius:.2f}°C")

    elif choice == '5':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        kelvin = (fahrenheit - 32) * 5/9 + 273.15
        print(f"{fahrenheit}°F is equal to {kelvin:.2f}K")

    elif choice == '6':
        kelvin = float(input("Enter temperature in Kelvin: "))
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        print(f"{kelvin}K is equal to {fahrenheit:.2f}°F")

    elif choice == '7':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 7.")
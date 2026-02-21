# Prime number checker
# step 1 : checck single number -----
number = int(input("Enter a number : "))
if number < 2:
    print(f"{number} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

        # step 2 : check a range of prime numbers -----
range_start = int(input("Enter the start of the range: "))
range_end = int(input("Enter the end of the range: "))

print(f"Prime numbers : ", end="")
for n in range(range_start, range_end + 1):
    if n >= 2:
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                bnt(n, end=" ")


C:\Users\MUTURAJ S\OneDrive\Desktop\Assignment 2            
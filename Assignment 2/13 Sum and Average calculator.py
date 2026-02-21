#create a sum and average calculator

count = int(input(" How many numbers?: "))
total_sum = 0
maximum= None
minimum= None

for i in range(count):
    number = float(input(f"Enter number {i + 1}: "))
    total_sum += number

    if maximum is None or number > maximum:
        maximum = number

    if minimum is None or number < minimum:
        minimum = number 

average = total_sum / count

# Display the results
print(f"\nTotal Sum: {total_sum}")
print(f"Average: {average}")    
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")

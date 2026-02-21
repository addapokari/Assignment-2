# Bill Splitter Program

#create a restaurant bill splitter program

# get the total bill amount and number of people
total_bill_amount = float(input("Enter the total bill amount: "))
num_people = int(input("Enter the number of people splitting the bill: "))
tax_percentage = float(input("Enter the tax percentage: "))
tip_percentage = float(input("Enter the tip percentage: "))

# calculations
subtotal = total_bill_amount / (1 + tax_percentage / 100)
tax_amount = subtotal * (tax_percentage / 100)
bill_after_tax = subtotal + tax_amount
tip_amount = bill_after_tax * (tip_percentage / 100)
total_bill= bill_after_tax + tip_amount
amount_per_person = total_bill / num_people

# display the results
print("\n=== Bill Summary ===")
print(f"Total Bill Amount: ${total_bill_amount:.2f}")
print(f"number of people: {num_people}")
print(f"tax percentage: {tax_percentage}%")
print(f"tip percentage: {tip_percentage}%")

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax Amount: ${tax_amount:.2f}")
print(f"Bill after Tax: ${bill_after_tax:.2f}")
print(f"Tip Amount: ${tip_amount:.2f}")
print(f"Total Bill: ${total_bill:.2f}")
print(f"Amount per person: ${amount_per_person:.2f}")
# Ticket Pricing System

# create a movie ticket pricing system.

age = int(input("Enter your age: "))
day= input("Enter the day of the week (e.g., Monday, Tuesday, etc.): ").lower()
tickets= int(input("Enter the number of tickets: "))
 
 # Determine base price by age
if age < 3:
    base_price = 0
elif 3 <= age <= 12:
    base_price = 150
elif 13 <= age <= 59:
    base_price = 300
else:
    base_price = 200    

    # Determine discount based on day and monday to thursday no discount,friday to sunday 20% discount
if day in ['friday', 'saturday', 'sunday']:
    discount_rate = 0.20
else:    
    discount_rate = 0.0


    # Calculate price
discounted_price = base_price * discount_rate
price_after_discount = base_price - discounted_price
total_amount = price_after_discount * tickets

# Display the results
print("\n=== Ticket Pricing Summary ===")
print("\nBase price :", base_price)
print("Discount amount:", discounted_price)
print("Price after discount: ", price_after_discount)
print("total amount :", total_amount)





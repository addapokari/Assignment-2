# simple ATM simulator
# create an ATM simulator with initial balance of 1000
check_balance = 1000
while True:
    print("\n=== Welcome to the ATM Simulator ===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print(f"Your current balance is: ${check_balance:.2f}")

    elif choice == '2':
        deposit_amount = float(input("Enter the amount to deposit: "))
        check_balance += deposit_amount
        print(f"${deposit_amount:.2f} deposited successfully. New balance: ${check_balance:.2f}")

    elif choice == '3':
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        if withdraw_amount > check_balance:
            print("Insufficient funds! Transaction cancelled.")
        else:
            check_balance -= withdraw_amount
            print(f"${withdraw_amount:.2f} withdrawn successfully. New balance: ${check_balance:.2f}")

    elif choice == '4':
        print("Thank you for using the ATM Simulator. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
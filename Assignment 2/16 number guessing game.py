import random

best_score = None  # Track minimum attempts

while True:
    number = random.randint(1, 100)
    attempts_left = 7
    attempts_used = 0

    print("\n Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print("You have 7 attempts to guess it.")

    while attempts_left > 0:
        guess = int(input("\nEnter your guess: "))
        attempts_used += 1
        attempts_left -= 1

        if guess == number:
            print(f"\n Congratulations! You guessed the number in {attempts_used} attempts.")
            
            # Track best score
            if best_score is None or attempts_used < best_score:
                best_score = attempts_used
                print(" New Best Score!")
            
            break

        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")

        # Bonus hint (within 5)
        if abs(guess - number) <= 5:
            print(" Very close!")

        if attempts_left > 0:
            print(f"Attempts remaining: {attempts_left}")

    else:
        print(f"\n Game Over! The number was {number}")

    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing! ")
        break

# Show best score at end
if best_score is not None:
    print(f"\n Best Score (minimum attempts): {best_score}")
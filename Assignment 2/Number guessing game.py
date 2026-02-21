# Number guessing game

import random
best_score = 0

while True:
    number = random.randint(1, 100)
    attempts_left = 5
    attempts_used = 0
    print("\nWelcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print("You have 5 attempts to guess the number.")
    while attempts_left > 0:
        guess = int(input("Enter your guess: "))
        attempts_used += 1
        attempts_left -= 1

        if guess == number:
            print(f"Congratulations! You've guessed the number  in {attempts_used} attempts!")
            # track best score

            if best_score is None or attempts_used < best_score:
                best_score = attempts_used
                print("New best score!")
            break
        elif guess >  number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")
            # bonus hint (within 5 attempts)
            if abs(guess - number) <= 5:
                print("Hint: You're very close!")
                if attempts_left > 0:
                    print(f"attempts left: {attempts_left}")
    else:
        print(f"Game over! The number was {number}.")
    # ask to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break
# display best score
if best_score is not None:
    print(f"Your best score (minimum attempts to guess correctly) is: {best_score}")




               

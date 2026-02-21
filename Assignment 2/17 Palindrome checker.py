# Palindrome checker
# take input from user
user_input = input("Enter a word/number: ")
# store original input
original = user_input
#   covert to lowercase for cheching (ignore case)
processed= user_input.lower()
# reverse the string
reversed_input = processed[::-1]
# display step by step
print(f"Original input: {original}")
print(f"Reversed input: {reversed_input}")

# check if palindrome
if processed == reversed_input:
    print(f"{original} is a palindrome.")
else:    
    print(f"{original} is not a palindrome.")


    
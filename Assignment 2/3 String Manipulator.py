# string manipulator program

# create a string variable

my_string = "Welcome to the Generative AI course!"

# caluculations

total_chars_with_spaces = len(my_string)
total_chars_without_spaces = len(my_string.replace(" ", ""))
total_words = len(my_string.split())

upper_case = my_string.upper()
lower_case = my_string.lower()
title_case = my_string.title()
first_word = my_string.split()[0]
last_word = my_string.split()[-1]
reversed_string = my_string[::-1]

# display the results

print(f"Original String: {my_string}")      
print(f"Total characters (with spaces): {total_chars_with_spaces}")
print(f"Total characters (without spaces): {total_chars_without_spaces}")
print(f"Total words: {total_words}")
print(f"Uppercase: {upper_case}")
print(f"Lowercase: {lower_case}")
print(f"Title Case: {title_case}")
print(f"First word: {first_word}")
print(f"Last word: {last_word}")
print(f"Reversed String: {reversed_string}")    

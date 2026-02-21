# text ananlysis functions
# 1.count words(text) - return number of words in a text
def count_words(text):
    words= text.split() 
    return len(text.split())
# 2.count vowels(text) - return number of vowels in a text
def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count=0
    for char in text:
        if char in vowels:
            count += 1
    return count
# 3. count consonants(text) - return number of consonants in a text
def count_consonants(text):
    vowels = 'aeiouAEIOU'
    count=0
    for char in text:
        if char.isalpha() and char not in vowels:
            count += 1
    return count
# 4. reverse_text(text) - return reversed text 
def reverse_text(text):
    return text[::-1]
# 5. is_palindrome(text) - return True/False
def is_palindrome(text):
    cleaned= text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
# 6. remove vowels(text) - return text without vowels
def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    result= ""
    for char in text:        
        if char not in vowels:
            result += char
    return result
# 7. word_frequency(text) - return a dictionary of word counts
def word_frequency(text):
    words = text.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency
# 8. longest_word(text) - return the longest word in the text
def longest_word(text):
    words = text.split()
    longest= max(words, key=len)
    return longest 
# 9. analyze_text(text) - calls all above functions and displays results
def analyze_text(text):
    print(f"===TEXT ANALYSIS===:\n")
    
    print(f"words:", count_words(text))
    print(f"vowels:", count_vowels(text))
    print(f"consonants:", count_consonants(text))
    print(f"reversed text:", reverse_text(text))
    
    if is_palindrome(text):
        print(f"palindrome: Yes")
    else:
        print(f"palindrome: No")

    print(f"text without vowels:", remove_vowels(text))
    longest= longest_word(text)
    print(f"longest word:", longest, f"({len(longest)} letters)")
    freq= word_frequency(text)
    print(f"word frequency:", end="")
    for word, count in freq.items():
        print(f" {word}({count})", end="")  
    print()

    # main function to test
    text= input("Enter text for analysis: ")
    analyze_text(text)
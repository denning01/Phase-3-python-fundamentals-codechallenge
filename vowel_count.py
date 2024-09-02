def count_vowels(text):
    # Define a set of vowels
    vowels = set("aeiou")
    # Convert text to lowercase to ignore case
    text = text.lower()
    # Initialize a counter for vowels
    count = 0
    
    # Loop through each character in the text
    for char in text:
        # If the character is a vowel, increment the counter
        if char in vowels:
            count += 1
    
    return count

# Allow user input

user_input = input("PUT A WORD OR TEXT: ")

# Call the function and display the result
print(f"The number of vowels is: {count_vowels(user_input)}")

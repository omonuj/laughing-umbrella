def count_vowels_and_consonants(input_string):
    vowels = "aeiouAEIOU"
    # Initialize counters
    vowel_count = 0
    consonant_count = 0
    
   
    for char in input_string:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count

# Main program
if __name__ == "__main__":
    # Collect input from the user
    user_input = input("Enter a string: ")
    
    # Count vowels and consonants
    vowels, consonants = count_vowels_and_consonants(user_input)
    
    # Display the results
    print(f"The input string contains {vowels} vowels and {consonants} consonants.")

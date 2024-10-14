#this program takes letters and digits and prints how many letters and how many digits.

#defining and setting function
def count_letters_and_digits(sentence_digits):

	#initialize variables to zero
	letters = 0
	digits = 0

	#for statement and if statement to check if if input is alphabet or digits and store them seperately  
	for char in sentence:
		if char.isalpha():
			letters += 1
		elif char.isdigit():
			digits += 1
		
#print letters and digits
	print(f"LETTERS {letters}")
	print(f"DIGITS {digits}")

#prompt user for inputs
sentence = input("Enter a sentence & digits: ")
count_letters_and_digits(sentence)

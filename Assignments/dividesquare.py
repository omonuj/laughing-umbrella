import math

def divide_or_square(number):

	if number % 5 == 0:
		return math.sqrt(number)
	else:
		return number % 5



if __name__ == "__main__":
	
	try:
		user_input = float(input("Enter a number: "))
		
		result = divide_or_square(user_input)
		print(f"The result is: ", result)
	except ValueError:
		print("Invalid input. Please enter a valid number. ")
		
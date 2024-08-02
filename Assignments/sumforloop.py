def sum_for_loop(list):

	total = 0
	
	for number in list:

		total += number

	return total

def main():
	numbers = [23, 34, 45, 45, 67, 65]
	print("Original list:", numbers)

	sum_for_loop(numbers)
	print("Sum using for loop:", sum_for_loop(numbers))

	
if __name__ == "__main__": 
	main()
def sum_while_loop(list):

	total = 0;
	index = 0;
	
	while index < len(list):
		
		total += list[index]
		
		index += 1
		
	return total

def main():
	numbers = [ 23, 45, 56, 67, 78]
	print("Original list: ", numbers)

	sum_while_loop(numbers)
	print("Sum using while loop: ", sum_while_loop(numbers))

	
if __name__ == "__main__":
	main()


	
	
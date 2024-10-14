def sum_do_while_loop(list):

	total = 0
	index = 0

	if len(list) > 0:

		while True:
			total += list[index]
			index += 1
			if index >= len(list):
				break
	return total

def main():

	numbers = [90, 23, 43, 54, 76, 19]
	print("Original list: ", numbers)

	sum_do_while_loop(numbers)
	print("Sum of numbers are: ", sum_do_while_loop(numbers))

if __name__ == "__main__":
	main()
	
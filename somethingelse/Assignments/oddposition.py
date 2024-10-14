def odd_positions(list):

	for index in range (len(list)):
		if index % 2 == 1:
			print(list[index])

numbers = [6, 7, 9, 20, 15, 3, 4]
print(odd_positions(numbers))

			
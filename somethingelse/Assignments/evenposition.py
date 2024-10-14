def even_positions(list):

	for index in range (len(list)):
		if index % 2 == 0:
			print(list[index])

numbers = [6, 7, 9, 20, 15, 3, 4]
print(even_positions(numbers))

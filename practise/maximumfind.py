def find_max(numbers):

	if len(numbers) == 0:
		return None

	max_number = numbers[0]
	for number in numbers:
		if number > max_number:
			max_number = number
	return max_number

numbers = [5, 2, 8, 8, 9, 14,89, 38]
print(find_max(numbers))

empty_list= []
print(find_max(empty_list))
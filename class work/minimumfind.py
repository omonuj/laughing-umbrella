def find_min(numbers):

	if len(numbers) == 0:
		return None

	min_number = numbers[0]
	for number in numbers:
		if number < min_number:
			min_number = number
	return min_number

numbers = [5, 2, 8, 8, 9, 14,89, 38]
print(find_min(numbers))

empty_list= []
print(find_min(empty_list))
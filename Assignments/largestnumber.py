def find_largest_element(number_list):

	largest_element = number_list[0]

	for element in number_list:
		if element > largest_element:
			largest_element = element
	return largest_element

numbers = [343, 23, 54, 675, 76, 454]
largest_element = find_largest_element(numbers)
print(f"The largest number in list is:",largest_element)

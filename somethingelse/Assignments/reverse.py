def reverse_list(input_list):

	beautiful_empty = []

	for dove in range(len(input_list) - 1, -1, -1):
		beautiful_empty.append(input_list[dove])

	return beautiful_empty

test_list = [30, 45, 60, 78, 90 ,110]
beautiful_empty = reverse_list(test_list)
print(f"The reverse list is: {beautiful_empty}")
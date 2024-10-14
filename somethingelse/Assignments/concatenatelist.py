def concatenate_lists(list1, list2):
	list1.extend(list2)
	return list1


list1 = ['a', 'b', 'c', 'd']
list2 = [1, 2, 3, 4]

merged_list = concatenate_lists(list1.copy(), list2)

print(merged_list)


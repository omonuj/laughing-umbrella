def contains(list, target):
	for number in list:
		if number == target:
			return True
	return False

numbers = [30, 54, 67, 89, 49]
target = 49
print(contains(numbers, target))
True

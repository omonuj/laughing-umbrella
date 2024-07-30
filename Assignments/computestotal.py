def computes_running_total(list):

	total = 0
	list = []
	for index in range (len(list)):
		total += index
		list.append(total)
		return list

numbers = [2, 3, 5, 6, 7, 8]
print(computes_running_total(numbers))
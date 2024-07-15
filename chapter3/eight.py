numbers = []

for user_input in range (4):
	digits = int(input("Enter a number: "))
	numbers.append(digits)

	sum_values = sum(numbers)
	average = sum_values / 4

	product = 1
	for digits in numbers:
		product *= digits

	minimum = min(numbers)
	maximum = max(numbers)


print(f"sum of numbers are:", {sum_values})
print(f"average of numbers are:", {average})
print(f"product of numbers are: ", {product})
print(f"minimum number is: ", {minimum})
print(f"maximum number is: ", {maximum})

#list = [4, 4, 6, 7, 7,]
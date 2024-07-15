number = int(input("Enter a five digit integer: "))

divide = 10000

while divide >= 1:
	digit = number // divide
	print(digit, end='    ')
	number = number % divide
	divide = divide // 10

print ()
	




number = int(input("Enter a number: "))

if number % 4 == 0:
	print("This number is a multiple of 4")
elif number % 2 == 0:
	print("This number is a multiple of 2")
else:
	print("This is an odd number")
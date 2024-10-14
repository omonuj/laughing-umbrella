number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))
number3 = int(input("Enter number3: "))

sum = number1 + number2 + number3
average = sum / 3 
product = number1 * number2 * number3


print("the average is: ", average)
print("the sum is: ", sum)
print("the product is: ", product)

if number1 < number2 or number1 < number3:
	print("number1 is the smallest")
elif number2 < number1 or number2 < number3:
	print("number2 is the smallest")
elif number3 < number1  or number3 < number2:
	print("number3 is the smallest ")



if number1 > number2 or number1 > number3:
	print("number1 is the largest")
elif number2 > number1 or number2 > number3:
	print("number2 is the largest")
elif number3 > number1  or number3 > number2:
	print("number3 is the largest ")




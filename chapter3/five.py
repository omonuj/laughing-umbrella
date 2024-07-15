"""comparing integers using if else statements and comparing operators """
print('Enter two integers, and i will tell you', 'the relationship they satisfy.')

number1 = int(input('Enter first number: '))

number2 = int(input('Enter second number: '))

number3 = int(input('Enter third number: '))

if number1 == number2:
	print(number1, 'is equal to', number2)
else: 
	print(number1, 'is not equal to', number2)
if number1 < number2:
	print(number1, 'is less than', nuumber2)
else:
	print(number1, 'is grester than', number2)
if number1 <= number2:
	print(number1, 'is less than or equal to', number2)
else:
	print(number1, 'is greater than or equal to', number2)



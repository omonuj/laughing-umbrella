#this program prompt user for integral inputs in string and computes the sum
def sum_strings():
   
	#prompt user for inputs
	user_input = input("Enter two interal numbers separated by a space: ")

	#splits the inputs into two with the splits method
	num1, num2 = user_input.split()
	
	#converts inputs strings to integers
	int_num1 = int(num1)
	int_num2 = int(num2)

	
	#computes the result back ti a string
	result = int_num1 + int_num2

	#converts results back to strinf
	return str(result)


#function call to executes the code in sum_strings
sum_result = sum_strings()

#prints out the result
print(f"The sum is: {sum_result}")
	

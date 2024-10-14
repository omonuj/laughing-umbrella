def only_floats(a, b):

	if isinstance(a, float) and isinstance(b, float):
		return 2
	
	elif isinstance(a, float) or isinstance(b, float):
		return 1
	
	else:
		return 0

if __name__ == "__main__":

	input_a = input("Enter the first value: ")
	input_b = input("Enter the second value: ")

	
	try:
		a = float(input_a)
	except ValueError:
		a = input_a

	try: 
		b = float(input_b)
	except ValueError:
		b = input_b

	result = only_floats(a, b)
	print(f"Result:", result)
	
	

	
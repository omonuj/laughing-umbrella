input('What is your problem?: ')

user_input = input("Have you had this problem before (yes or no)? ")

if user_input == "yes":
	print('well, you have it again')
elif  user_input == "no":
	print('well, you have it now')
else:
	print("Please answer with 'yes' or 'no'.")
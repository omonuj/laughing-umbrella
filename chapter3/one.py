validatinguserinput = 0
score = 0
while score != 1 and score != 2:
	score = int (input("Enter number other than 1 or 2 to exit : "))
	if score != 1 and score != 2: 
		validatinguserinput = validatinguserinput + 1
print(validatinguserinput)
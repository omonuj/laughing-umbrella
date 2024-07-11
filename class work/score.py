score = int(input("Enter your score: "))

if score >= 75 <= 100:
	print("A")
elif score >= 65 <= 74:
	print("B")
elif score >= 50 <= 64:
	print("C")
elif score >= 40 <= 49:
	print("D")
elif score <= 39 <= 0:
	print("F")

print(score)
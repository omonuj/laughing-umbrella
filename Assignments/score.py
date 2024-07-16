for score in range (15):
	score = int(input("Enter a score: "))

sum_pass = 0
sum_fail = 0
pass_mark = 45

if score >= 45:
	sum_pass += score
else:
	sum_fail += score

print(f"number of students that pass are:", {sum_pass})
print(f"number of students that fail are:", {sum_fail})
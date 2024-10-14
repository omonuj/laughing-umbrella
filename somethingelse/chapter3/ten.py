principal = int(input("Enter amount to invest: "))

rate_of_return = 0.12

years = int(input("Enter period in years: "))

for period in range (1, years+1):
	amount = principal * (1 + rate_of_return) ** period
	print(f"After {period} years, the amount on deposit will be: #{amount:.2f}")
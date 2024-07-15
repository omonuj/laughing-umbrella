principal = 1000

rate_of_return = 0.07

years = [10, 20, 30]

for period in years:
	amount = principal * (1 + rate_of_return) ** period
	print(f"After {period} years, the amount on deposit will be: #{amount:.2f}")
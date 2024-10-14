#program that converts minutes inputed to years and #days

#defines a method for years and days
def years_and_days(minutes):

	#initializes variables to be used in the function that stores values
	start = minutes / 60
	sum_days = start / 24
	years = int(sum_days / 365)
	days = sum_days % 365
	
#returns years and days, 
	return years, days

#collects input from user in minutes
minutes = int(input("Enter minutes: "))

#initializes years and days to the function
years, days = years_and_days(minutes)

#prints the result fro years and days
print(f"{minutes}minutes makes {years}years and {days}days")







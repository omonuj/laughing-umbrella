#a program that reads numbers in feet and convert them to meters.

#reads input from user as feets
feets = int(input("Enter feet: "))

#create a constant for multiplying feets
constant_foot = 0.305

#converts feets to meters
meters = feets * constant_foot

#prints out the result
print(f"{feets}feets converted to Meters is: {meters}meters")
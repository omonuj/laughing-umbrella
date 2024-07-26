#This proram reads inputs from a user as form of lenth and radius, and it 
# computes the area and volume of a cylinder.

	#reads input from user for length and radius
radius = int(input("Enter radius: "))
length = int(input("Enter length : "))

#declare the value of pie as 3.14156 approximately.
pi = 3.1416

#define area.
area = pi * radius ** 2

#define colume
volume = area * length

print(f"The area is:  {area} while the volume is: {volume}")

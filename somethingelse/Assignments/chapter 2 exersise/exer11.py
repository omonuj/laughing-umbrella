number = input("Enter a five-digit integer: ")

if len(number) != 5 or not number.isdigit():
    print("Invalid input. Please enter a five-digit integer.")
else:
    
    print(f"{number[0]}   {number[1]}   {number[2]}   {number[3]}   {number[4]}")
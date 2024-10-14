def get_sortedNumbers():
    # Prompt the user to enter three numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    
    # Store the numbers in a list
    numbers = [num1, num2, num3]
    
    # Sort the list
    numbers.sort()
    
    # Display the sorted numbers
    print(f"The numbers in increasing order are: {numbers[0]}, {numbers[1]}, {numbers[2]}")

if __name__ == "__main__":
    get_sortedNumbers()

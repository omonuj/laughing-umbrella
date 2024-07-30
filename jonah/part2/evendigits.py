#This program generates lists of even numbers from 1000 t0 3000

#defines method
even_digit_numbers = []

for number in range(1000, 3001):
    # Convert the number to a string
    num_str = str(number)
    # Assume all digits are even initially
    all_even = True
    
    # Check each digit to see if it is even
    for digit in num_str:
        if int(digit) % 2 != 0:
            all_even = False
            break
    
    # If all digits are even, add the number to the list
    if all_even:
        even_digit_numbers.append(num_str)

#uses the join method to join the list into a single string with each number separated by a comma
result = ",".join(even_digit_numbers)

#prints results
print(result)

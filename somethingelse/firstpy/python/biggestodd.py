def biggest_odd(numbers_string):
    biggest = None
    for char in numbers_string:
        numb = int(char)
        if numb % 2 != 0:
            if biggest is None or numb > biggest:
                biggest = numb

    return biggest


num = input("Enter a number: ")
blue = biggest_odd(num)
print(f"The biggest oddnumber is: {blue}")
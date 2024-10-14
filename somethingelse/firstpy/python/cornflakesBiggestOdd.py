def biggest_odd(numbers_string):
    biggest = None
    for char in numbers_string:
        numb = int(char)
        if numb % 2 != 0:
            if biggest is None or numb > biggest:
                biggest = numb

    return biggest
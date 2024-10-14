def get_strings(str_first, str_last):

    str_first_swapped = str_last[:2] + str_first[2:]
    str_last_swapped = str_first[:2] + str_last[2:]

    result = str_first_swapped + " " + str_last_swapped

    return result

str_first = "hello"
str_last = "hil"

print(get_strings(str_first, str_last))

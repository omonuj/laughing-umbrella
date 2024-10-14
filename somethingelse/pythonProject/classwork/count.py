from collections import Counter


def count_characters(input_string):
    char_frequency = Counter(input_string)
    return dict(char_frequency)

input_string = "semicolon.africa"
print(count_characters(input_string))
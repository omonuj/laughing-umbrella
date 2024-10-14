def count_char_occurences(word, char):

    word = word.lower()
    char = char.lower()

    count = word.count(char)
    return (char, count)

print(count_char_occurences("semicolon", "o"))
print(count_char_occurences("hellooo", "o"))
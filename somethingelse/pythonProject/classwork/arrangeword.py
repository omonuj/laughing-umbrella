def arrange_word(word):
    middle_index = len(word) // 2

    if len(word) % 2 == 0:
        return word[:middle_index].upper() + word[middle_index:].lower()
    else:
        return word[:middle_index + 1].upper() + word[middle_index + 1:].lower()

print(arrange_word('helloworld'))
print(arrange_word('fried'))
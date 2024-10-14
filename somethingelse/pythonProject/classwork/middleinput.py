def middle_input_ce(word):
    middle_index = len(word) // 2

    if len(word) % 2 == 0:
        return word[:middle_index] + "ce" + word[middle_index:]
    else:
        return word + "ce"

print(middle_input_ce("helloo"))
print(middle_input_ce("world"))
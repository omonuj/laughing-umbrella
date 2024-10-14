empty_list = []

for number in range(1, 10):
    empty_list += [number]

    print(number)

letters = []

letters += "burble"

print(letters)

list1 = [20, 30, 40, 50]
list2 = [10, 34, 55]

sum = sum(list1)
sum2 = list1 + list2
print(f"the results are: {sum} {sum2}")


def cube_list(values):

    for num in range (len(values)):
        values[num] **= 3

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

cube_list(number)

print(cube_list(number))

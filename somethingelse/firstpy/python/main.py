numbers = list(range(1, 101))

def multiples_of_five(n):
    if n % 5 == 0:
        return n


outcome = []
for number in numbers:
    if multiples_of_five(number):
        outcome.append(number)

print(outcome)

x = [[0 for _ in range(4)] for _ in range(5)]

print(x)

array = [0] * 5
array2 = [array] * 5
print (array2)

for i in range(5):
    for j in range(4):
        x[i][j] = 8
        print(x[i][j])


score = (2, 4, 6, "abum")

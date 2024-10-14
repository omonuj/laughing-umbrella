number = int(input("Enter a number to create its multiplication table: "))

print(f"Multiplication table for {number}:")
for base in range(1, 10):
    print(f"{number} x {base} = {number * base}")
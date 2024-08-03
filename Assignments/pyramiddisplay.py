def main():
    while True:
        try:
            n = int(input("Enter an integer from 1 to 13: "))
            if 1 <= n <= 13:
                break
            else:
                print("Please enter a number between 1 and 13.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    for i in range(1, n + 1):
       
        print(" " * (n - i), end="")
        

        for j in range(i, 0, -1):
            print(j, end="")
        
       
        for j in range(2, i + 1):
            print(j, end="")
        
        print()

if __name__ == "__main__":
    main()

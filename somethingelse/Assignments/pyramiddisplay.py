def main():
    while True:
        try:
            user = int(input("Enter an integer from 1 to 13: "))
            if 1 <= user <= 13:
                break
            else:
                print("Please enter a number between 1 and 13.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    for index in range(1, user + 1):
       
        print(" " * (user - index), end="")
        

        for column in range(index, 0, -1):
            print(column, end="")
        
       
        for column in range(2, index + 1):
            print(column, end="")
        
        print()

if __name__ == "__main__":
    main()

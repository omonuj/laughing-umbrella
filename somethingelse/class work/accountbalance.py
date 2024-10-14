stop = 1
balance = 0

while stop != 0:
    user_input = int(input("Enter 1 to deposit or 2 to withdraw: "))
    if user_input == 1:
        deposit = int(input("Enter deposit amount: "))
        balance = deposit + balance
    if user_input == 2:
        withdrawal = int(input("Enter withdrawal amount: "))
        balance = balance - withdrawal
    #else: 
        #print("invalid input try again")
        
    stop = int(input("Enter 0 to stop or 1 to continue"))

net_balance = balance
print('the net balance is:', net_balance)


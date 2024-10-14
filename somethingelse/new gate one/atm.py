accounts = []
pins = []
balances = []

while True:
    print("""	
		Welcome to Gtb ATM
		Main Menu:
    		1. Create Account
    		2. Close Account
    		3. Deposit Money
    		4. Withdraw Money
    		5. Check Balance
    		6. Change PIN
		7. transfer money
    		8. Exit
	""")
    choice = input("Choose an option: ")

    if choice == "1":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        pin = input("Enter PIN: ")

        account_id = first_name + last_name

        if account_id in accounts:
            print("Account already exists.")
        else:
            accounts.append(account_id)
            pins.append(pin)
            balances.append(0.0)
            print("Account created successfully.")
            print(f"Account ID: {account_id}")
            print(f"PIN: {pin}")

    elif choice == "2":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        pin = input("Enter PIN: ")

        account_id = first_name + last_name

        if account_id in accounts:
            index = accounts.index(account_id)
            if pins[index] == pin:
                del accounts[index]
                del pins[index]
                del balances[index]
                print("Account closed successfully.")
            else:
                print("Incorrect PIN.")
        else:
            print("Account not found.")

    elif choice == "3":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        pin = input("Enter PIN: ")

        account_id = first_name + last_name

        if account_id in accounts:
            index = accounts.index(account_id)
            if pins[index] == pin:
                amount = float(input("Enter amount to deposit: "))
                balances[index] += amount
                print(f"Deposit successful. New balance: #{balances[index]}")
            else:
                print("Incorrect PIN.")
        else:
            print("Account not found.")

    elif choice == "4":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        pin = input("Enter PIN: ")

        account_id = first_name + last_name

        if account_id in accounts:
            index = accounts.index(account_id)
            if pins[index] == pin:
                amount = float(input("Enter amount to withdraw: "))
                if amount <= balances[index]:
                    balances[index] -= amount
                    print(f"Withdrawal successful. New balance: #{balances[index]}")
                else:
                    print("Insufficient balance.")
            else:
                print("Incorrect PIN.")
        else:
            print("Account not found.")

    elif choice == "5":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        pin = input("Enter PIN: ")

        account_id = first_name + last_name

        if account_id in accounts:
            index = accounts.index(account_id)
            if pins[index] == pin:
                print(f"Current balance: #{balances[index]}")
            else:
                print("Incorrect PIN.")
        else:
            print("Account not found.")

    elif choice == "6":
       	first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        pin = input("Enter current PIN: ")

        account_id = first_name + last_name

        if account_id in accounts:
            index = accounts.index(account_id)
            if pins[index] == pin:
                new_pin = input("Enter new PIN: ")
                pins[index] = new_pin
                print("PIN changed successfully.")
            else:
                print("Incorrect PIN.")
        else:
            print("Account not found.")
    elif choice == "7":
       	first_name = input("Enter sender's first name: ")
        last_name = input("Enter sender's last name: ")
        pin = input("Enter sender's PIN: ")

        sender_account_id = first_name + last_name
        
        first_name = input("Enter receiver's first name: ")
        last_name = input("Enter receiver's last name: ")
        receiver_account_id = receiver_first_name + receiver_last_name
        
        sender_account = None
        receiver_account = None
        
        for account in accounts:
            if account["account_id"] == sender_account_id and account["pin"] == sender_pin:
                sender_account = account
            if account["account_id"] == receiver_account_id:
                receiver_account = account
        
        if sender_account and receiver_account:
            amount = float(input("Enter amount to transfer: "))
            if amount <= sender_account["balance"]:
                sender_account["balance"] -= amount
                receiver_account["balance"] += amount
                print("Transfer successful. New balance for sender: #", sender_account["balance"])
            else:
                print("Insufficient balance in sender's account.")
        else:
            print("Invalid account details for transfer.")

    elif choice == "8":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
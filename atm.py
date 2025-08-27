def atm():
    pin = 1234
    balance = 10000
    attempts = 0
    while attempts < 3:
        entered_pin = int(input("Enter your ATM PIN: "))
        if entered_pin == pin:
            while True:
                print("\n1. Check Balance\n2. Withdraw Cash\n3. Deposit Cash\n4. Exit")
                choice = int(input("Select an option: "))
                if choice == 1:
                    print(f"Your current balance is: ${balance}")
                elif choice == 2:
                    amount = float(input("Enter amount to withdraw: "))
                    if amount <= balance:
                        balance -= amount
                        print(f"Please take your cash: ${amount}")
                        print(f"Your current balance is: ${balance}")
                elif choice == 3:
                    amount = float(input("Enter amount to deposit: "))
                    balance += amount
                    print(f"Successfully deposited: ${amount}")
                    print(f"Your current balance is: ${balance}")
                elif choice == 4:
                    print("Thank you for using the ATM.")
                    return
                else:
                    print("Invalid option. Please try again.")
        else:
            attempts += 1
            print(f"Incorrect PIN. You have {3 - attempts} attempts left.")
    print("Too many incorrect attempts. Your card is blocked.")
# User inputs here
atm=atm()

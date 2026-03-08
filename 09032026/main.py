# create a banking system
balance = 0

def deposit():
    global balance
    deposit_amount = int(input("How much would you like to deposit?"))
    if deposit_amount > 0:
        balance += deposit_amount
        print(f"Deposited ${deposit_amount}. New balance: ${balance}")
    else:
        print("Deposit amount must be positive")
    

def withdraw():
    global balance
    withdraw_amount = int(input("How much would you like to withdraw?"))
    if withdraw_amount > balance:
        print("Insufficient funds")
    elif withdraw_amount <= 0:
        print("Withdrawal amount must be positive")
    else:
        balance -= withdraw_amount
        print(f"Withdrew: ${withdraw_amount}. New balance ${balance}")

def show_balance():
    global balance
    print(f"Current balance: ${balance}")

def banking_system():
    while True:
        print("\n--- Banking menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            deposit()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            show_balance()
        elif choice == "4":
            print("Thank you for using the banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4")

banking_system()
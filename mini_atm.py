# Mini ATM Program

PIN = "1234"
balance = 10000

# PIN Verification
attempts = 3

while attempts > 0:
    entered_pin = input("Enter your PIN: ")

    if entered_pin == PIN:
        print("\nLogin Successful!\n")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. Attempts left: {attempts}")

if attempts == 0:
    print("Too many incorrect attempts. Account locked.")
else:
    while True:
        print("\n=====================")
        print("        ATM")
        print("=====================")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Your balance is KSh {balance}")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))

            if amount <= 0:
                print("Invalid amount. Deposit must be greater than zero.")
            else:
                balance += amount
                print(f"Deposit successful! New balance: KSh {balance}")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Invalid amount. Withdrawal must be greater than zero.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print(f"Withdrawal successful! New balance: KSh {balance}")

        elif choice == "4":
            print("Thank you for using our ATM!")
            break

        else:
            print("Invalid option. Please try again.")
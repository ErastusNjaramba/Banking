class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"KES {amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"KES {amount} withdrawn successfully.")
            else:
                print("Error: Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Your current balance is: KES {self.balance}")

def main():
    print("Welcome to Python ATM!")
    name = input("Please enter your name: ")
    try:
        initial_balance = float(input("Please enter your initial balance: "))
    except ValueError:
        print("Invalid balance entered, setting balance to 0.")
        initial_balance = 0
    
    user_account = Account(name, initial_balance)
    print("\nAccount created successfully!\n")

    while True:
        print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            try:
                amount = float(input("Enter deposit amount: "))
                user_account.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

        elif choice == 2:
            try:
                amount = float(input("Enter withdrawal amount: "))
                user_account.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        
        elif choice == 3:
            user_account.check_balance()

        elif choice == 4:
            print("Thank you for using Python ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

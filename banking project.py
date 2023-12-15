class BankAccount:
    def __init__(self, account_holder, balance=0, pin=None):
        self.account_holder = account_holder
        self.balance = balance
        self.pin = pin

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs.{amount}. New balance: Rs.{self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew Rs.{amount}. New balance: Rs.{self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def set_pin(self, pin):
        if pin is not None and 1000 <= pin <= 9999:
            self.pin = pin
            print("PIN set successfully.")
        else:
            print("Invalid PIN. Please choose a 4-digit PIN.")

    def verify_pin(self, pin):
        return self.pin == pin


# Function to create a bank account
def create_account():
    account_holder = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance: Rs."))
    pin = int(input("Set a 4-digit PIN: "))
    return BankAccount(account_holder, initial_balance, pin)


# Function to perform transactions
def perform_transactions(account):
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Change PIN\n5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            amount = float(input("Enter the amount to deposit: Rs."))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: Rs."))
            account.withdraw(amount)
        elif choice == '3':
            print(f"Account balance for {account.account_holder}: Rs.{account.balance}")
        elif choice == '4':
            new_pin = int(input("Enter new 4-digit PIN: "))
            account.set_pin(new_pin)
        elif choice == '5':
            print("Exiting online banking. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# Main program
if __name__ == "__main__":
    # Create a bank account
    account = create_account()

    # Log in using PIN
    entered_pin = int(input("Enter your 4-digit PIN to log in: "))
    if account.verify_pin(entered_pin):
        print(f"Login successful. Welcome, {account.account_holder}!")
        # Perform transactions
        perform_transactions(account)
    else:
        print("Incorrect PIN. Exiting online banking.")

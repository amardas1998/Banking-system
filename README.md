# Banking-system
A banking system is a complex software and financial infrastructure that facilitates a variety of financial services, including managing accounts, processing transactions, and providing various financial products. Below is a description of the key components and features typically found in a banking system:

1. BankAccount Class:

The BankAccount class represents a bank account and has the following attributes:

account_holder: The name of the account holder.
balance: The current balance in the account.
pin: A 4-digit PIN for account authentication.
The class includes methods for:

__init__(self, account_holder, balance=0, pin=None): The constructor initializes the account with the account holder's name, an optional initial balance (default is 0), and an optional PIN (default is None).
deposit(self, amount): Deposits a specified amount into the account.
withdraw(self, amount): Withdraws a specified amount from the account if sufficient funds are available.
set_pin(self, pin): Sets a new PIN for the account.
verify_pin(self, pin): Verifies whether the entered PIN matches the account's PIN.
Functions:

2. create_account(): Prompts the user to enter details for creating a new bank account, including the account holder's name, initial balance, and a 4-digit PIN. Returns a BankAccount object.
perform_transactions(account): Displays a menu for the user to perform transactions such as depositing, withdrawing, checking the balance, changing the PIN, or exiting the program.
Main Program:

The program begins by creating a new bank account using the create_account() function.
The user is prompted to enter a 4-digit PIN to log in.
If the entered PIN matches the account's PIN (verified using verify_pin), the user is welcomed, and transactions can be performed using the perform_transactions function.
The user can deposit money, withdraw money, check the balance, change the PIN, or exit the program.
Security Consideration:

The PIN is used as a simple form of authentication. However, in a real-world scenario, more secure authentication methods, such as encryption and secure password storage, would be necessary.
User Interaction:

The program uses input() to interact with the user through the console, allowing them to enter information and make choices.

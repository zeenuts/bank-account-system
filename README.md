# Bank Account System

A simple banking system I built while learning Object-Oriented Programming (OOP) in Python.

## What it does
- Creates bank accounts with an owner name and initial balance
- Lets you deposit money into accounts
- Lets you withdraw money from accounts
- Keeps track of all transactions (deposits and withdrawals)
- Shows your current balance
- Displays complete transaction history

## Features
-  Create bank accounts
-  Deposit money (with validation)
-  Withdraw money (with validation)
-  View account balance
-  View transaction history
-  Prevent negative amounts
-  Prevent overdrafts (withdrawing more than you have)

## How to use it

```python
from bank_account import BankAccount

# Create a new account
account = BankAccount("Your Name", 1000)

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(200)

# Check your balance
account.show_balance()

# View all transactions
account.show_history()

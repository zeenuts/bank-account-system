from bank_account import BankAccount

# Demo 1: Basic operations
print("=== Demo 1: Basic Operations ===")
account = BankAccount("John Doe", 1000)
account.deposit(500)
account.withdraw(200)
account.show_balance()
account.show_history()

# Demo 2: Another account
print("\n=== Demo 2: Different Account ===")
account2 = BankAccount("Jane Smith", 2000)
account2.deposit(1000)
account2.withdraw(500)
account2.show_history()

# Demo 3: Test edge cases
print("\n=== Demo 3: Edge Cases ===")
account3 = BankAccount("Bob", 100)
print("Attempting to deposit negative amount:")
account3.deposit(-50)
print("Attempting to withdraw more than balance:")
account3.withdraw(200)
print("Attempting to withdraw negative amount:")
account3.withdraw(-30)

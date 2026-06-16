class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []
    
    def deposit(self,amount):
        if amount <= 0:
            print("The Amount Must Be Positive And Above Zero.")
            return
        self.balance+=amount
        self.history.append(f"Deposited: ${amount}")
        print(f"Deposited: ${amount} | Current Balance: ${self.balance}")
    
    def withdraw(self,amount):
        if amount <= 0:
            print("The Amount Must Be Positive And Above Zero.")
            return
        if amount > self.balance:
            print(f"Insufficient funds as the amount exceeds your current balance that is ${self.balance}")
            return
        self.balance-=amount
        self.history.append(f"Withdrawn: ${amount}")
        print(f"Withdrawn: ${amount} | Current Balance: ${self.balance}")
    
    def show_balance(self):
        print(f"Current Balance: ${self.balance}")
    
    def show_history(self):
        if not self.history:
            print("You haven't made any transactions yet.")
            return
        print("---Transactions---")
        for entry in self.history:
            print(entry)
        print(f"Total Transactions: {len(self.history)}")

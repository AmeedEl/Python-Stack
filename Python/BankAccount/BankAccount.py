class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee.")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
    

account1 = BankAccount(int_rate=0.02, balance=100)
account2 = BankAccount(int_rate=0.03, balance=200)

account1.deposit(50).deposit(25).deposit(75).withdraw(100).yield_interest().display_account_info()
account2.deposit(100).deposit(50).withdraw(25).withdraw(40).withdraw(10).withdraw(20).yield_interest().display_account_info()

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
    
class User: 
    def __init__(self, name):
        self.name = name
        self.account = BankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, ", end="")
        self.account.display_account_info()
        return self
    
user1 = User("Tamam")
user2 = User("Mansour")

user1.make_deposit(100).make_deposit(50).make_withdrawal(30).account.yield_interest().display_account_info()
user2.make_deposit(200).make_withdrawal(50).make_withdrawal(25).account.yield_interest().display_account_info()
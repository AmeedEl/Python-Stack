class User:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount
        return self
    
    def make_withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f"Insufficient balance for {self.name}.")
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")
        return self
    
    def transfer_money(self, other_user, amount):
        if amount <= self.balance:
            self.balance -= amount
            other_user.balance += amount
            print(f"Transferred ${amount} from {self.name} to {other_user.name}.")
        else:
            print(f"Insufficient balance to transfer for {self.name}.")
        return self
    

user1 = User("User One", 150)
user2 = User("User Two", 300)
user3 = User("User Three", 500)


    # User1 makes 3 deposits and 1 withdrawal
user1.make_deposit(50).make_deposit(100).make_deposit(80).display_user_balance()

    # User2 makes 2 deposits and 2 withdrawals
user2.make_deposit(200).make_deposit(50).make_withdrawal(100).make_withdrawal(150).display_user_balance()

    # User3 makes 1 deposit and 3 withdrawals 
user3.make_deposit(100).make_withdrawal(50).make_withdrawal(100).make_withdrawal(80).display_user_balance()

    # BONUS: 
user1.transfer_money(user3, 100)
user1.display_user_balance()
user3.display_user_balance()
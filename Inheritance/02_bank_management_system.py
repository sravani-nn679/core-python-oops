class Bank:
    def __init__(self, balance):
        self.balance=balance
    def deposit(self, amount):
        self.balance=self.balance+amount
    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance=self.balance-amount
        else:
            print("invalid balance")
    def check_balance(self):
        print(self.balance)
class User(Bank):
    def __init__(self, balance, name):
        self.name=name
        super().__init__(balance)
        print("account holder:sravs")
u=User(1000,"sravs")
u.deposit(1000)
u.withdraw(500)
u.check_balance()



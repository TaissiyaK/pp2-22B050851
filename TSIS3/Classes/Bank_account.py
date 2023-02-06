class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self):
        print("print the sum you want to put on deposit")
        sum_put = int(input())
        self.balance += sum_put
        return Account(self.owner, self.balance)
    def withdraw(self):
        print("print sum of money you want to take")
        sum_take = int(input())
        while sum_take > self.balance:
            print("print sum of money you want to take")
            sum_take = int(input())
        self.balance -= sum_take
        return Account(self.owner, self.balance)
    def __str__(self):
        return f"{self.owner} has {self.balance} on deposit"


account = Account(input(),int(input()))
account = Account.deposit(account)
account = Account.withdraw(account)
print(account)
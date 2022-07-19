class Account:

    def __init__(self, name):
        self.balance = 0
        self.name = name

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("negative deposit not allowed")
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("negative deposit not allowed")
        self.balance = self.balance - amount

    def transfer(self, amount, account):
        if amount < 0:
            raise ValueError("negative transfer not allowed")
        self.balance = self.balance - amount
        account.balance = account.balance + amount


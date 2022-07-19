class Shopping:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):


    def withdraw(self, amount):
        if amount < 3000:
            raise valueError("you can not buy more than three things")





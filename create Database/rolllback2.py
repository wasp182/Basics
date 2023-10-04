from decimal import *

class account():

    _qb=Decimal("0.00")
    def __init__(self,name:str,open_balance: float =0):
        self.name = name
        self.balance = Decimal(open_balance).quantize(account._qb)
        print("account opened for {}".format(name))
        self.show_balance()

    def deposit(self,amount)-> Decimal:
        decimal_amount = Decimal(amount).quantize(account._qb)
        if decimal_amount > 0:
            self.balance += decimal_amount
            print("{} deposited in account".format(decimal_amount))
        return self.balance

    def withdraw(self,amount):
        decimal_amount = Decimal(amount).quantize(account._qb)
        if self.balance - decimal_amount >= 0 :
            self.balance -= decimal_amount
            print("{} withdrawal from account".format(decimal_amount))
            return decimal_amount
        else: print("amount should be less than your account balance")
        return account._qb

    def show_balance(self):
        print("balance for {} is {}".format(self.name,self.balance))


if __name__=='__main__':
    john = account('john')
    john.deposit(110)
    john.deposit(150)
    john.withdraw(55)
    john.show_balance()
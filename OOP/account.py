import datetime, pytz

class Account:

    # create static method -- remove self and put annotation
    @staticmethod
    def _current_time():
        utc_time=datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    # adding transaction  list to account details
    def __init__(self,name,balance):
        #below can be changed by direct method without calling deposit and withdrawal
        # we need to make below static outside the class - non public
        self._name=name
        self._balance= balance
        self._transaction_list=[(Account._current_time(), balance)]
        print("account created for " + name)

    def deposit(self, amount):
        if amount>0:
            self._balance+=amount
        self.show_balance()
        self._transaction_list.append((Account._current_time(), amount))

    def show_transaction_details(self):
        for date , amount in self._transaction_list:
            if amount>0:
                txn_type = "Deposit"
            else:
                txn_type="Withdrawal"
            print(f"{txn_type} : {amount} ON {date.astimezone()}"  )


    def withdraw(self,amount):
        if self._balance-amount>0:
            self._balance-=amount
            self._transaction_list.append((Account._current_time(), -amount))
        else: print("Withdrawal must be less than balance amount")
        self.show_balance()


    def show_balance(self):
        print("Balance is {}".format(self._balance))


if __name__ =="__main__":
    myAccount = Account("S",100)
    myAccount.deposit(150)
    myAccount.withdraw(1540)
    myAccount.show_transaction_details()


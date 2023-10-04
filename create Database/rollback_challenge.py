import datetime
import sqlite3
import pytz
import pickle

db = sqlite3.connect("accounts.sqlite3",detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("create table if not exists accounts (name Text Primary key not null,balance Integer Not null)")
db.execute("create table if not exists history (time timestamp not null,"
           "account text not null,amount integer not null,zone integer not null, Primary key(time,account) )")
db.execute("create view if not exists localhistory AS "
           " select strftime('%Y-%m-%d %H:%M:%f',history.time,'localtime')AS localtime,"
           " history.account,history.amount from history order by history.time ")

class account():
    def __init__(self,name:str,open_balance: int =0):
        cursor=db.execute("select name,balance from accounts where (name=?)",(name,))
        row = cursor.fetchone()
        if row:
            self.name , self.balance = row
            print("account retrieved for {}".format(name))
        else:
            self.name= name
            self.balance = open_balance
            cursor.execute("insert into  accounts values(?,?)",(name,open_balance))
            cursor.connection.commit()
            print("account opened for {}".format(name))
        self.show_balance()

    @staticmethod
    def _current_time():
        # return pytz.utc.localize(datetime.datetime.utcnow())
        utc_time = pytz.utc.localize(datetime.datetime.utcnow())
        local_time = utc_time.astimezone()
        zone = local_time.tzinfo
        return utc_time,zone

    def deposit(self,amount: int)-> float:
        if amount > 0:
            self.save_update(amount)
            print("{:.2f} deposited in account".format(amount/100))
        return self.balance/100

    def withdraw(self,amount: int)-> float:
        if self.balance - amount >= 0 :
            self.save_update(-amount)
            print("{:.2f} withdrawal from account".format(amount))
            return amount/100
        else: print("amount should be less than your account balance")
        return 0

    def show_balance(self):
        print("balance is {}".format(self.balance/100))

    def save_update(self,amount):
        new_balance = self.balance + amount
        deposit_time , zone = account._current_time()
        picked_zone = pickle.dumps(zone)
        db.execute("update accounts set balance=? where (name=?)",(new_balance,self.name))
        db.execute("insert into history values(?,?,?,?)",(deposit_time,self.name,amount,picked_zone))
        db.commit()
        self.balance = new_balance




if __name__=='__main__':
    john = account('john')
    john.deposit(110)
    john.deposit(150)
    john.withdraw(55)
    john.show_balance()
    max = account('max')
    max.deposit(55)
    max.withdraw(88)
    terry = account('terry')
    terry.deposit(55)
    db.close()

import sqlite3

db = sqlite3.connect("contacts.sqlite")
# creates a database if it doesnt already exists
db.execute("create table if not exists contacts(name text, phone integer, email text)")
db.execute("insert into contacts values('swapnil',555,'swpanil@gmail.com')")

cursor = db.cursor()
cursor.execute("select * from contacts ")

# dd fetchone and fetchall to get records in list one by one or together
print(cursor.fetchone())
print(cursor.fetchall())
print(cursor.fetchone())

for name, phone, email in cursor:
    print(name,phone,email)
    print('*'*80)

cursor.close()
# a database cursor is iterable so we used a for loop
# cursor is a generator , it is iterable that can move to next value without runming out of memory
# theoretically we can count to infinity without having to run out of memory
# if we copy another loop here we will not getting any output

db.commit()
db.close()



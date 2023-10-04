import sqlite3

db= sqlite3.connect("contacts.sqlite")

# this email and phone no is hard coded , we can use parameters instead
new_mail= "swapniltyagi@gmail.com"
phones = input('please enter a phone number')
# if this input has sql statements in it then

# update_sql="update contacts set email='{0}' where phone={1}".format(new_mail,phones)
update_sql="update contacts set email=? where phone= ?"
# above lines allows python lib to sanitze the input values ans protect itself from sql injection attacks
print(update_sql)

update_cursor = db.cursor()
# update_cursor.execute(update_sql)
#below can execute multiple scripts or statements separated by colon
# we can input the new queries in the update cursor
update_cursor.execute(update_sql,(new_mail,phones))

print("no of rows updated {}".format(update_cursor.rowcount))

# update_cursor.connection.commit()
update_cursor.close()

# iterating over database without having to create a cursor
# db.execute("insert into contacts values('swapnil',555,'swpanil@gmail.com')")
#sql lite wraps insert and creations in end of transactions
# all previous inserts are rolled back from previous transactions
# a transaction will be committed once all changes are valid, commit changes in previous script
for rows in db.execute("select * from contacts"):
    print(rows)

db.close()
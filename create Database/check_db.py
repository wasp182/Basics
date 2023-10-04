import pytz
import sqlite3

db= sqlite3.connect("accounts.sqlite3",detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("select localtime from localhistory "):
    print(row)
    # convert the string time to actual datetime using pytz
    # utc_time = row[0]
    # local = pytz.utc.localize(utc_time).astimezone()
    # print("{}\t{}".format(utc_time,local))


db.close()

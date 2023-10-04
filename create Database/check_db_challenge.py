import pytz
import sqlite3
import pickle

db= sqlite3.connect("accounts.sqlite3",detect_types=sqlite3.PARSE_DECLTYPES)

for row in db.execute("select * from history "):
    # print(row)
    # convert the string time to actual datetime using pytz
    utc_time = row[0]
    zone=row[3]
    selected_zone = pickle.loads(zone)
    local = pytz.utc.localize(utc_time).astimezone(selected_zone)
    print("{}\t{}\t{}".format(utc_time,local,local.tzinfo))


db.close()

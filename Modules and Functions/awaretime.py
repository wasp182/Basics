import pytz
import datetime

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Local time (naieve) {}".format(local_time))
print("UTC time (naieve) {}".format(utc_time))

#aware time zones

# local_time_aware = pytz.utc.localize(local_time)
# we should only work with UTC time zone and localise the time while printing
local_time_aware = pytz.utc.localize(utc_time).astimezone()
utc_time_aware = pytz.utc.localize(utc_time)

print("local time {}".format(local_time_aware))
print("UTC  time {}".format(utc_time_aware))

# how utc time can copy with daylights changes better than local time

gap_time = datetime.datetime(2015,10,25,1,30,0,0)
print(gap_time.timestamp())
d1 = gap_time.timestamp()
d2 = d1 + 3600

tz1= pytz.timezone('Asia/Kolkata')

dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(d1)).astimezone(tz1)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(d2)).astimezone(tz1)

print(dt1)
print(dt2)
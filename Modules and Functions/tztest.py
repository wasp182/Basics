import time

import pytz
import datetime

country = 'Europe/Moscow'
tz_object = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_object)

print("time in {} right now : {}".format(country, local_time))


print("*"*80)
#
# for x in pytz.all_timezones:
#     print(x)
#
# for x in sorted(pytz.country_names):
#     print(x + ": "+ pytz.country_names[x])
#
# for x in sorted(pytz.country_names):
#     print(x + " {} : {} ".format(pytz.country_names[x],pytz.country_timezones[x]))
#
# print("*"*80)

for x in sorted(pytz.country_names):
    print(x+ " : "+ pytz.country_names[x] )
    if x in pytz.country_timezones:
        for zones in pytz.country_timezones[x]:
            time_z = pytz.timezone(zones)
            local_time_disp = datetime.datetime.now(time_z)
            print(" {} : {}".format(zones,local_time_disp))
    else:
        print("no time zone")




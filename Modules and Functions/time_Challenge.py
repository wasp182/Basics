# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.
import datetime

import pytz

available_timezones = {
    "1":"Africa/Tunis",
    "2":"Asia/Kolkata",
    "3":"Australian/Adelaide",
    "4":"Europe/Brussels",
    "5":"Europe/London",
    "6": "Japan",
    "7": "Pacific/Tahiti",
    "8": "US/Hawaii",
    "9": "Zulu"
}

print("Choose from below list or choose 0 to quit")
for items in available_timezones:
    print("{} : {} ".format(items,available_timezones[items]))

while  True:
    choice= input(": ")
    if choice == "0":
        break
    if choice in available_timezones:
        tz_disp = pytz.timezone(available_timezones[choice])
        world_time = datetime.datetime.now(tz=tz_disp)
        print(" TIme in {} is {} {}".format(available_timezones[choice],world_time.strftime("%A %x %X %z"),world_time.tzinfo))

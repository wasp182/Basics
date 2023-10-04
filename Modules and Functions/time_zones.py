import time

print("epoch time: {}".format(time.strftime('%c',time.gmtime(0))))
print("currenet time xone:" + time.tzname[0])

if time.daylight != 0 :
     print("daylight savings time is {} ".format(time.tzname[1]))

print("local time is :" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print("GMT time is :" + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
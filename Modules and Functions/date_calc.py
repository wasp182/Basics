from time import perf_counter as my_time
import random
import time

print(time.gmtime(0))
print(time.localtime())
print(time.time())

time_here = time.localtime()
print('year:',time_here[0],time_here.tm_year)
print('month:',time_here[1],time_here.tm_mon)
print('date:',time_here[2],time_here.tm_mday)

#tm_here.tm_year is a named tuple here

input("press enter")
wait_time = random.randint(1,6)
time.sleep(wait_time)
start_time = my_time()
input('press enter to stop')
stop_time = my_time()

print("started at "+ time.strftime("%X",time.localtime(start_time)))
print("reaction time {}".format(stop_time-start_time))
import timeit
import functools

# reduce calls the fucntion passed repeatedly till there are no arguments left

def cal_val(x,y):
    return x+y

numbers = [2,3,4,5,6]

reduced_values = functools.reduce(cal_val,numbers)
print(reduced_values)

# reduce works like this
res = cal_val(2,3)
res = cal_val(res,4)
res = cal_val(res,5)
res = cal_val(res,6)
print(res)


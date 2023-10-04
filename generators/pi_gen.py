import math

def odd_gen():
    x = 1
    while True:
        yield x
        x = x + 2

# odds = odd_gen()
# # function isnt really called at line 7 , it is called at line 9
# print(next(odds))
# print(next(odds))
# print(next(odds))
# print(next(odds))
# print(next(odds))

def alt_sign():
    x = -1
    while True:
        x *= -1
        yield x

def pi_inf(n):
    odds = odd_gen()
    odds_list =[]
    sign = alt_sign()
    pi4_val = 0
    # print(odds,alt_sign,odds_list)
    for i in range(n):
        values = (next(sign))*(next(odds))
        odds_list.append(values)
    # print(odds_list)
    for values in odds_list:
        pi4_val += 1/values
    return pi4_val*4

# for i in range(250):
#     print(pi_inf(i))

def pi_gen():
    odds = odd_gen()
    pi_val = 0
    while True:
        pi_val += (4/next(odds))
        yield pi_val
        pi_val -= (4/next(odds))
        yield pi_val

pi = math.pi
pi_gen = pi_gen()
for n in range(100000):
    print("{:.5f} % difference".format(((pi - next(pi_gen))/pi)*100))





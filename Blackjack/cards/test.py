for i in range(1,13):
    print("No {0:2} square is {1:4} and cube is {2:4}".format(i,i**2,i**3))

# width of output can also be specified with colon after replacement field index {N:M} , foield no N with M spaces

for i in range(1,13):
    print("No {0:-1} square is {1:-3} and cube is {2:-4}".format(i,i**2,i**3))


#Below can give left aligned outputs
for i in range(1,13):
    print("No {0:2} square is {1:<3} and cube is {2:<4}".format(i,i**2,i**3))

print('pi is approx {0:12}'.format(22/7))
print('pi is approx {0:12f}'.format(22/7))
# gives default 6 digits after decimal -- pi is approx     3.142857
print('pi is approx {0:12.50f}'.format(22/7))
# 50 digits after decimal , igmnores 12
print('pi is approx {0:<52.50f}'.format(22/7))
# max precision in pythoon is bw 51 and 52 , hence only return till 50 decimal points
print('pi is approx {0:<62.50f}'.format(22/7))
print('pi is approx {0:<72.50f}'.format(22/7))
print('pi is approx {0:<72.54f}'.format(22/7))
# padded with zeros after 50th precision - pi is approx 3.142857142857142793701541449991054832935333251953125000
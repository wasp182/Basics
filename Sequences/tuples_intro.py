data1="a","b","c"
print(data1)
#data1[1]="v"
data2=list(data1)
print(data2)
print(type(data1))
print(type(data2))

# Unpacking a tuple

x,y,z = 1,2,3
print(x)
print(y)
data3=11,22,33
print('unpacking a tuple')
x,y,z=data3
print(x)
print(y)
# x, y , z are not tuples but (1,2,3) is the tuple
# list can also be assigned as x,y ,z = list_data3
# i.e. 
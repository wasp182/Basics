data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

# del data[0:2]
# print(data)
#
# del data[16:]
# print(data)

#does nothing as position of last two values has changed

# asssume values should be bw 100 and 200
# cant use for loop to simply remove items as for  iterates lists using an index function that gets updated to next value
# in case one item is removed , subsequent item will be skipped as index moves to next index +1 however the old index
# has moved one behind and hence skipped entirely

# DELETING ITERABLES WITH FOR LOOP is not advisable
# DONT USE THE INDEX CONTROL IN FOR LOOP AS INDEX IS RESET EVEYTIME WE MOVE TO FOR LOOP LINE AGAIN

min_valid = 100
max_valid = 200

#removing low values from start of ORDERED list

stop = 0
for index,item in enumerate(data):
    if item >= min_valid:
        stop= index
        break
print(data)
del data[:stop]
print(data)

# remving hihg values from sorted list

start = 0;
# Referring a list in reverse
# first -1 refers to include the first item in list as range excldues the second index , if we uised 0 then first item
#would have been ignored,
# Second -1 refers to increment of -1
for index in range(len(data)-1,-1,-1):
    if data[index]<= max_valid:
        #position of last desirable input is given above
        start=index + 1
        # +1 added cause we want to keep the last acceptable index and start remvign from next index onwards
        break
print(data)
del data[start:]
print(data)





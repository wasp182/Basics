data = [102,522,142,200,140,5,1,44,166]
min_valid= 100
max_valid =200

# for index in range(len(data)-1,-1,-1):
#     if data[index]<min_valid or data[index] > max_valid:
#         print("index no: {0} \nremoved no: {1}".format(index,data[index]))
#         del data[index]
#         print(data)
# print(data)
#
# Reversed fucntion for backward iteration
max_index = len(data)
for index,value in enumerate(reversed(data)):
    print(index,value)
    if value < min_valid or value > max_valid:
        print("removing index: {0} in data: {1}".format(index,data))
        del data[max_index-index]
print(data)

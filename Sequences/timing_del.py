import timeit

max_len=10000
min_valid=990
max_valid=9990

# data1=range(max_len)
# data2=range(max_len)
# data3=range(max_len)
# above wont work since range doesnt work as list function hence we need to change the type as below
data1=list(range(max_len))
data2=list(range(max_len))
data3=list(range(max_len))

def sanitise_ordered_Removal(data):
    stop=0
    for index,value in enumerate(data):
        if value>=min_valid:
            stop=index
            break
    del data[:stop]

    start=len(data)
    for index in range(len(data)-1,-1,-1):
        if data[index]<=max_valid:
            start=index+1
            break
    del data[start:]

def sanitise_reversed(data):
    top_index=len(data)-1
    for index,value in enumerate(reversed(data)):
        if value>max_valid or value < min_valid:
            del data[top_index-index]

def sanitise_simple_backward_Iteration(data):
    for index in range(len(data)-1,-1,-1):
        if data[index]>max_valid or data[index] < min_valid:
            del data[index]

if __name__=="__main__":
    print("timings")
    t1=timeit.timeit("sanitise_ordered_Removal(data1)",
                     setup="from __main__ import sanitise_ordered_Removal,"
                           "data1",
                     number=1)
    print("ordered removal : {}".format(t1))
    t2=timeit.timeit("sanitise_reversed(data2)",
                     setup="from __main__ import sanitise_reversed,"
                           "data2",
                     number=1)
    print("Reversed method: {}".format(t2))
    t3=timeit.timeit("sanitise_simple_backward_Iteration(data3)",
                     setup="from __main__ import sanitise_simple_backward_Iteration,"
                           "data3",
                     number=1)
    print("simple backward iteration: {}".format(t3))

    # sanitise_ordered_Removal(data1)
    # sanitise_reversed(data2)
    # sanitise_simple_backward_Iteration(data3)
    # print(data1)
    # print(data2)
    # print(data3)

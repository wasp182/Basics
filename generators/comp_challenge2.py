import timeit

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

def nested_loop():
    for locs in sorted(locations):
        list_locs = []
        for x in exits:
            if locs in exits[x].values():
                list_locs.append([locs , x])
        print(list_locs)


def loop_com():
    for locs in sorted(locations):
        list_locs_comp = [(locs,x) for x in exits if locs in exits[x].values() ]
        print(list_locs_comp)


def nest_comp():
    list_nested = [print([(locs , x) for x in exits if locs in exits[x].values()])
                    for locs in locations]
    # for loc in list_nested:
    #     print(loc)

############################### TIMEIT ###############################
#
# res1 = timeit.timeit(loop_code,number=1000,globals=globals())
# res2 = timeit.timeit(comp_code,number=1000,globals=globals())
# res3 = timeit.timeit(nested_comp_code,number=1000,globals=globals())
#
# print(res1)
# print(res2)
# print(res3)

###################### using setup in timeit instead###################
setups = """\
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}
# """
results=[]
for i in range(1000,10000,1000):
    res_1 = timeit.timeit(nested_loop,number=i,setup=setups)
    res_2 = timeit.timeit(loop_com,number=i,setup=setups)
    res_3 = timeit.timeit(nest_comp,number=i,setup=setups)
    results.append((res_1,res_2,res_3))

print(results)


final = [[i for i in range(len(items)) if min(items) == items[i] ]for items in results]
file = "Results2.text"
with open(file,'a') as res_file:
    print(final,file=res_file)

# print("nested loops : {}".format(res_1))
# print("comp : {}".format(res_2))
# print("nested comps : {}".format(res_3))
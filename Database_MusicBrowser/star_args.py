def average(*args):
    print(args)
    print(*args)
    mean =0
    for i in args:
        mean += i
    return mean/len(args)

print(average(1,2,3,4))
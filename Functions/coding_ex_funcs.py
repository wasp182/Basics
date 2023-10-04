def sum_eo(n,t):
    total=0
    if t.casefold()=='e':
        for i in range(1,n):
            if i%2==0:
                total+=i
    elif t.casefold()=='o':
        for i in range(1,n):
            if i%2!=0:
                total+=i
    else: return -1
    return total

print(sum_eo(5,'o'))

def sum_eo_efficient(n,t):
    if t == "e":
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, n, 2))


print(sum_eo_efficient(5,'o'))

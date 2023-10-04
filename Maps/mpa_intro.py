import timeit


text = " hello to this world"

def caps():
    capitals = [x.upper() for x in text]
    return capitals

def map_caps():
    map_caps = list(str(map(str.upper,text)))
    return map_caps

def cap_words():
    cap_words = [x.upper for x in text.split(" ")]
    return cap_words

def map_words():
    map_words = list(str(map(str.upper,text.split(" "))))
    return map_words


res1 = timeit.timeit(caps,number=1000,globals=globals())
res2 = timeit.timeit(map_caps,number=1000,globals=globals())
res3 = timeit.timeit(cap_words,number=1000,globals=globals())
res4 = timeit.timeit(map_words,number=1000,globals=globals())

print(res1)
print(res2)
print(res3)
print(res4)
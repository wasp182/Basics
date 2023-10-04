import sys

def my_range(n : int):
    start = 0
    while start < n:
        print(f"value from generator {start}")
        yield start
        start += 1

rng = my_range(5)
# rng is a generator
print("Size of Range is {}".format(sys.getsizeof(rng)))

big_list = []
for v in rng:
    _ = input("Line 16")
    big_list.append(rng)

print("Size of big list is {}".format(sys.getsizeof(big_list)))
print(rng)
print(big_list)

print("will below loop start ?...No")
for i in rng:
    print(i)

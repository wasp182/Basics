nums= (1,2,3,4,5)

print(nums)
print(*nums)

def test_args(*args):
    print(args)
    for i in args:
        print(i)


test_args(nums)
# if you add print to above , it will return None because this func
# returns nothing
test_args(1,2,3)
test_args(4)
number_str = input('please enter three no separated by , ')
nums = number_str.split(sep=',')
for index in range(len(nums)):
    nums[index]=int(nums[index])
a,b,c=nums
print(a+b-c)
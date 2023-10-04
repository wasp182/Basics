even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

empty_list=[]

nums = even+odd

print(sorted(nums))
print(nums)

digits= sorted("984213")
print(digits)
unsorted = list("984651")
print(unsorted)

more_nums = list(nums)
print(more_nums)
print(id(nums))
print(id(more_nums))
print(nums is more_nums)

sliced_nums = nums[:]
print(nums is sliced_nums)

copied_list = nums.copy()
print(nums is copied_list)


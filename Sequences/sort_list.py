even=[2,4,6,8]
odd=[1,3,5,7,9]

# method 1
even.extend(odd)
print(even)
even.sort()
print(even)
even.sort(reverse=True)
print(even)
# O/p
# [2, 4, 6, 8, 1, 3, 5, 7, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [9, 8, 7, 6, 5, 4, 3, 2, 1]
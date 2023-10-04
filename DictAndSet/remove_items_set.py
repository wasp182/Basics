nums = set(range(21))

nums.remove(2)
nums.remove(9)

nums.discard(999)
nums.remove(990)

# discard wont throw exception if value is not found
# remove will throw exception since item is not in set



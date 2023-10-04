pangram="the quick brown fox jumps over the lazy dog"
letters= sorted(pangram)

print(letters)
nums = [2.3,6,6.7,6.89,9]
print(sorted(nums))
nums.sort()
print(nums)
# objects that modify object in its place return None
missing_letter= sorted("the quick brown fox jump over the lazy dog",key=str.casefold)
#NEVER USE PARANTHESIS IN SORTING FUNCTIONS AS WE ARE NOT CALLING IT , \
#ONLY TELLING SORTED FUCNTOIN WHICH METHOD TO CALL WHILE SORTING
print(missing_letter)

names= ['A','a','b','C','E','f']
names.sort()
print(names)
names.sort(key=str.casefold)
print(names)
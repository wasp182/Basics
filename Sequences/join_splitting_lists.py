pangram="the quick brown fox" \
        " jumps over the lazy dog"
print(pangram.split())

numbers="65,29,985,212,095,494"
# Challenge - convert them to list to integers

string_sample = (numbers.split(","))
print(string_sample)

# Method 1 - generators
print("".join(item if item not in ", " else " " for item in numbers))


# Method 2
int_list=[]
for item in string_sample:
    int_list.append(int(item))
print(int_list)

#Method 3
for index in range(len(string_sample)):
    string_sample[index]=int(string_sample[index])

print(string_sample)


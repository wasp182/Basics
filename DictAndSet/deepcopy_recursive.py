from deep_copy_ex import deep_copy
import copy

original = {
    "Tim": ["Buchalka", ["Programmer", "Teacher"]],
    "J-P": ["Roberts", ["Programmer", "Teacher"]],
}

copy1=copy.deepcopy(original)
copy2 = deep_copy(original)

original["Tim"].append("Aus")
print()
print(original)
print(copy1)
print(copy2)

original["Tim"][1].append("another one")
print()
print(original)
print(copy1)
print(copy2)

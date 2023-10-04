from data import plants_dict,plants_list,basic_plants_list

# this list is amde up of named tuples of type Plant referred by Var name of tuple
# i.e. named tuples can be created by var name which was given during declaration of named tuple
# type name cannot start with _ or nos
print(plants_list[0])

for plants in basic_plants_list:
    print(plants[0])

# for named tuples we can refer through field name

print("*"*80)
for plants in plants_list:
    print(plants.name)

# we can also change the fields values  using named tuples
print()

example = plants_list[0]
print(example.lifecycle)
example = plants_list[0]._replace(lifecycle="Annual")
print(example.lifecycle)

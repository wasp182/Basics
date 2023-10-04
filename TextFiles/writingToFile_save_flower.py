data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]


filename_towrite = 'flowers.txt'
with open(filename_towrite,'w') as plants:
    for plant in data:
        print(plant,file=plants)

new_list=[]
with open('flowers.txt','r') as data2:
    for lines in data2:
        new_list.append(lines.rstrip())

print(new_list)

filename_write = "flower_write.txt"
with open(filename_write,'w') as plants:
    for lines in data:
        plants.write(lines+"\n")

#trying to write numbers using print and write()

numbers_write = 'number_write.txt'
with open(numbers_write,'w') as nums:
    for i in range(10):
        print(i,file=nums)

with open(numbers_write,'w') as nums:
    for i in range(10):
        nums.write(str(i)+"\n")

#write() method will only write a string representation in text mode




import csv

file = 'cereal_grains.csv'

with open(file, 'r', encoding="utf-8", newline="") as inp_stream:
    readers = csv.DictReader(inp_stream)
    for lines in readers:
        print(lines)

import csv

filename = 'country_info.txt'
country={}
dialect = csv.excel
dialect.delimiter = "|"

with open(filename) as country_info:
    header = country_info.readline().strip("\n").split(dialect.delimiter)
    for index, item in enumerate(header):
        header[index] = item.casefold()
    country_dict = csv.DictReader(country_info,dialect=dialect,fieldnames=header)
    for items in country_dict:
        # print(items["Country"])
        # code_key =
        country[items["country"].casefold()] = items
        country[items["cc"].casefold()] = items

print(country)

while True:
    country_check = input("enter country name :").casefold()
    if country_check in country:
        print(country[country_check]["capital"])
    elif country_check == 'quit':
        break
    else:
        print("type quit to quit OR")
        continue



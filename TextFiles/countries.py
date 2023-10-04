filename = 'country_info.txt'
country={}

with open(filename) as country_info:
    first_line = country_info.readline()
    for lines in country_info:
        data = lines.strip('\n').split("|")
        name, capital, code , code3 , dialing , timezone, ccy = data
        country_dict={
            'name': name,
            'capital': capital,
            'code' : code,
            'code3' : code3,
            'dialing' : dialing,
            'timezone' : timezone,
            'ccy' : ccy,
        }
        country[name.casefold()]= country_dict
        country[code.casefold()] = country_dict

print(country)

# print(country)
while True:
    country_check = input("enter country name :").casefold()
    if country_check in country:
        print(country[country_check]["capital"])
    elif country_check == 'quit':
        break
    else:
        print("type quit to quit OR")
        continue



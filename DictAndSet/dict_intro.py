vehicles = {
            'dream': 'Honda 250T',
            'roadster': 'BMW R1100',
            'er5': 'Kawasaki ER5',
            'can-am': 'Bombardier Can-Am 250',
            'virago': 'Yamaha XV250',
            'tenere': 'Yamaha XT650',
            'jimny': 'Suzuki Jimny 1.5',
            'fiesta': 'Ford Fiesta Ghia 1.4',
            'roadster' : 'Triumph'
            }

# methods of retreiving info - using key instead
print(vehicles['dream'])
print(vehicles.get('jimny'))
#print(vehicles['dreams'])
# index crashes
#print(vehicles.get('draeem'))
# get function returns none


vehicles['fighter']='Lockheed F-104'

# for i in vehicles:
#     print(i,vehicles[i],sep=': ')

print()
for i,name in vehicles.items():
    print(i, name,sep=': ')

del vehicles['fighter']
print(vehicles)

result=vehicles.pop("fq",None)
print(result)
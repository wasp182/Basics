shoplist =['pasta','milk','spam','hello']
toFind='spam'
foundAt=0

for i in range(0,len(shoplist)+1):
    if shoplist[i]==toFind:
        foundAt=i
        break
print('{0} found at position no {1}'.format(toFind,foundAt+1))

if toFind in shoplist:
    foundAt=shoplist.index(toFind)
print('found at {}'.format(foundAt))
filename = 'Jabberwocky.txt'

with open('Jabberwocky.txt') as jabber:
    for lines in jabber:
        print(lines.strip())

print("*"*80)

with open('Jabberwocky.txt') as poem:
    first = poem.readline().strip()
    print(first)

# remove aprostrophe using Strip method
chars= "' Twasebv"
no_apos = first.strip(chars)
print(no_apos)

print("*"*80)

twas_remove = first.removeprefix("'Twas")
print(twas_remove)

toves_remove = first.removesuffix("toves")
print(toves_remove)

def my_removeprefix(string : str,pref : str) -> str:
    if string.startswith(pref):
        return string[len(pref):]
    else:
        return string


def my_removesuffix(string : str,suff : str) -> str:
    if string.endswith(suff):
        return string[:-len(suff)]
    else:
        return string


print("*"*80)
print(my_removesuffix(first,'toves'))

print("*"*80)
print(my_removeprefix(first,"'Twa"))

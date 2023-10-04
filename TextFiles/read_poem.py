# jabber = open('Jabberwocky.txt','r')
# print(jabber)
#
# for line in jabber:
#     # print(line)
#     #output in double space format
#     # print(line,end="")
#     # output in normal format
#     # print(line.strip(),end="")
#     # all output in single line as we stripped it of new line character
#     # end argument will prevent any new line inclusion
#     print(line.strip())
#     # this will return normal text
#     # strip will remove whitespace from begin and end of line
#     # use rStrip() strips from end of line only
#     # use lstrip() strip from beginor left  only
#
# jabber.close()
# # always close file
# # each new lone begins with new line character \n
# # pyhton wille xecute this character also hence the double spacing in o/p
# # or use python to remove whitespace character - tab , space and newline
# # python uses strip method to remove the whitespces and new line


with open('Jabberwocky.txt','r',encoding='utf-8') as jabber:
    # for line in jabber:
    #     print(line.strip())
# with ensures file terminates after end of block
#     lines = jabber.readlines()
    lines= jabber.read()

# readlines returns each line as entry to list separated by \n i.e. new line
print(lines)

for rev in reversed(lines):
    print(rev,end="")
    # print(rev,end="")

with open('Jabberwocky.txt') as jabber:
    while True:
        line = jabber.readline().strip()
        print(line)
        if 'jubjub' in line.casefold():
            break
print("*"*80)

with open('Jabberwocky.txt') as jabber:
    for line in jabber:
        print(line.strip())
        if 'jubjub' in line.casefold():
            break


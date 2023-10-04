# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

# Your code goes here ...

for item in text.casefold():
    if item.isalnum() :
        word_count[item]=word_count.setdefault(item,0)+1


# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)


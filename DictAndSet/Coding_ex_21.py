text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Add your code here.

set_words = set(text.split())
print(set_words)

set_words.intersection_update(prepositions)
print(set_words)
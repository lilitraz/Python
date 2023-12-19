# I'm using the words in words.txt to find anagrams in two ways:

# 1.

anagrams = {}

with open('words') as f:
    for line in f:
        word = line.strip()
        key = tuple(sorted(word))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]

print(anagrams)

for words in anagrams.values():
    print(' '.join(words))

# 2.

from collections import defaultdict

anagrams = defaultdict(list)

with open('words') as f:
    for line in f:
        word = line.strip()
        key = tuple(sorted(word))
        anagrams[key].append(word)

print(anagrams)

for words in anagrams.values():
    print(' '.join(words))


def groupby(iterable, key=lambda x: x):
    "Return a dict of {key(item): [items...]} grouping all the items in the iterable."
    groups = dict()
    for item in iterable:
        groups.setdefault(key(item), []).append(item)
    return groups


def sortedstr(word):
    return ''.join(sorted(word))


def anagram_table(words):
    return groupby(words, sortedstr).values()


anagrams = anagram_table('earth hater at heart stop post on pots no stop'.split())

print(anagrams)
# [['earth', 'hater', 'heart'], ['at'], ['stop', 'post', 'pots', 'stop'], ['on', 'no']]



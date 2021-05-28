
IS_WORD = '__end__'

def make_trie(words):
    root = dict()
    for word in words:
        current = root
        for c in word:
            current = current.setdefault(c, {})
        current[IS_WORD] = ''

    return root


def word_in_trie(trie, word):
    current = trie
    for c in word:
        if c not in current:
            return False
        current = current[c]

    return IS_WORD in current



root = make_trie(['foo', 'bar', 'baz', 'barz'])

print(root)
print(word_in_trie(root, list("bax")))
print(word_in_trie(root, list("bar")))
print(word_in_trie(root, list("barz")))

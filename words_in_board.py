# count words that can be formed in board using all 8 nbrs

IS_WORD = "__end__"

def make_trie(words):
    root = dict()
    for word in words:
        current = root
        for c in word:
            current = current.setdefault(c, {})
        current[IS_WORD] = ''

    return root


def get_indices(x, coll):
    return range(max(x - 1, 0), min(x + 2, len(coll)))

def gen_nbrs(board, i, j):
    for r in get_indices(i, board):
        for c in get_indices(j, board[0]):
            if not (i == r and j == c):
                yield r, c


def search(board, i, j, trie, visited, count):

    if (i, j) in visited:
        # dont reuse tiles in same word
        return

    if board[i][j] not in trie:
        # this tile is not part of any prefix
        return

    trie = trie[board[i][j]]

    if IS_WORD in trie:
        count[0] += 1
        # dont recount this word
        trie.pop(IS_WORD)

    visited = visited | {(i, j)}

    for r, c in gen_nbrs(board, i, j):
        search(board, r, c, trie, visited, count)


def search_words(board, words):
    trie = make_trie(words)

    count = [0]
    for i in range(len(board)):
        for j in range(len(board[0])):
            search(board, i, j, trie, set(), count)

    return count[0]


def find(board, i, j, trie, visited, prefix, found):

    if (i, j) in visited:
        return

    c = board[i][j]
    if c not in trie:
        return

    prefix = prefix + [c]
    visited = visited | {(i, j)}
    trie = trie[c]

    if IS_WORD in trie:
        found.add(''.join(prefix))

    for r, c in gen_nbrs(board, i, j):
        find(board, r, c, trie, visited, prefix, found)


def find_words(board, words):
    trie = make_trie(words)

    found = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            find(board, i, j, trie, set(), [], found)

    return found



board = [
    ["a", "b", "c", "d"],
    ["x", "a", "y", "z"],
    ["t", "z", "r", "r"],
    ["s", "q", "q", "q"]
]
words = ["bar", "car", "cat"]

print(find_words(board, words))

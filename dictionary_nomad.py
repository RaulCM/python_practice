from itertools import combinations
from collections import deque


def is_nbr(s1, s2):
    if len(s1) != len(s2):
        return False

    dist = (int(a != b) for a, b in zip(s1, s2))

    return sum(dist) == 1


def make_graph(words, n):
    adj_list = [[] for _ in range(n)]
    for i, j in combinations(range(n), 2):
        if is_nbr(words[i], words[j]):
            adj_list[i].append(j)
            adj_list[j].append(i)
    return adj_list

# when words are large generating and comparing nbrs on fly will TLE
# pre-compute adj_list with numeric vertex labels

def find_steps(dictionary, start, end):
    if len(start) != len(end):
            return -1
    if start == end:
        return 0

    words = words = list({w for w in dictionary if len(w) == len(start)} | {start, end})
    n = len(words)
    adj_list = make_graph(words, n)

    source = words.index(start)
    dest = words.index(end)

    queue = deque()
    queue.append((source, 0))
    visited = set()

    while len(queue):
        v, d = queue.popleft()
        if v == dest:
            return d

        visited.add(v)

        for u in adj_list[v]:
            if u not in visited:
                queue.append((u, d + 1))

    return -1

print(find_steps(["day", "soy"], "soy", "day"))

print(find_steps(["day", "soy", "say"], "soy", "day"))

from collections import deque


def gen_nbr(s):
    for i in range(len(s)):
        for c in range(97, 97 + 26):
            yield s[:i] + chr(c) + s[i + 1 :]


def find_steps(dictionary, start, end):
    if len(start) != len(end):
            return -1
    if start == end:
        return 0

    words = set(dictionary)
    queue = deque()
    queue.append((start, 0))
    visited = set()
    visited.add(start)

    while len(queue):
        v, d = queue.popleft()
        if v == end:
            return d

        for u in gen_nbr(v):
            if u not in visited and u in words:
                queue.append((u, d + 1))
                visited.add(u)

    return -1


print(find_steps(["day", "soy"], "soy", "day"))

print(find_steps(["day", "soy", "say"], "soy", "day"))


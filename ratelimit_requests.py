import collections

WIN_SIZE = 60

def process(req_ts, ts, limit, size):
    while len(req_ts) > 0 and ts - req_ts[0] >= size:
        req_ts.popleft()
    return len(req_ts) < limit


def count_served(requests, U, G):
    """2 rate-limits present user and global, count requests passing both"""

    requests.sort(key=lambda req: (req[1], req[0]))
    history = collections.defaultdict(collections.deque)
    ans = 0

    for uid, ts in requests:

        passed_u = process(history[uid], ts, U, WIN_SIZE)
        passed_g = process(history['global'], ts, G, WIN_SIZE)

        if passed_u and passed_g:
            history[uid].append(ts)
            history['global'].append(ts)
            ans += 1

    return ans


print(count_served([[0, 1],[0, 2]], 1, 5))
print(count_served([[0, 1],[0, 61]], 1, 5))
print(count_served([[0, 1],[1, 2], [2, 3]], 1, 2))
print(count_served([[0, 1],[0, 2], [1, 3], [1, 4]], 2, 4))

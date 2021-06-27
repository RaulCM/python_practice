from bisect import bisect_left


def lis_indices(nums, n):
    piles = []
    positions = {-1: -1}
    pred = [-1] * n

    for i, x in enumerate(nums):
        pos = bisect_left(piles, x)
        if pos == len(piles):
            piles.append(x)
        else:
            piles[pos] = x

        positions[pos] = i
        pred[i] = positions[pos - 1]

    result = []
    last_pos = positions[len(piles) - 1]
    while last_pos >= 0:
        result.append(last_pos)
        last_pos = pred[last_pos]

    return reversed(result)


def str_list(s):
    return list(map(int, s.split()))


# implicit pair with above by index, implied from statement coods are uniq
tests = [("2 5 8 10", "6 4 1 2"), ("5 3 10", "6 4 1"), ("1 2 3 4 5 6", "3 4 5 6 1 2")]


for n, s in tests:
    north = str_list(n)
    south = str_list(s)
    pairs = sorted(zip(north, south), key=lambda p: p[0])
    print(pairs)
    bridges = [pairs[i] for i in lis_indices(map(lambda p: p[1], pairs), len(south))]
    print(bridges)

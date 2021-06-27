from queue import PriorityQueue


def put(min_heap, arrays, r, i):
    if len(arrays[r]) > i:
        min_heap.put_nowait((arrays[r][i], r, i))


def merge(arrays):

    min_heap = PriorityQueue()

    for r in range(len(arrays)):
        put(min_heap, arrays, r, 0)

    acc = []
    # n log K
    while not min_heap.empty():
        top, r, i = min_heap.get_nowait()
        acc.append(top)
        put(min_heap, arrays, r, i + 1)

    return acc


def merge2(a1, a2):

    i = 0
    j = 0

    acc = []
    while i < len(a1) and j < len(a2):
        a = a1[i]
        b = a2[j]

        if a < b:
            acc.append(a)
            i += 1
        else:
            acc.append(b)
            j += 1

    while i < len(a1):
        acc.append(a1[i])
        i += 1

    while j < len(a2):
        acc.append(a2[j])
        j += 1

    return acc


def merge_recur(arrays):
    if len(arrays) == 0:
        return []

    if len(arrays) == 1:
        return arrays[0]

    acc = merge2(arrays[0], arrays[1])
    return merge_recur(arrays[2:] + [acc])  # O(k) copy :(


arrays = [[5, 7, 10], [3, 6, 8, 9], [0, 0, 1], [], [21], [4, 7, 13], [2, 4, 6, 8, 10]]

print(merge(arrays))
print(merge_recur(arrays))

# given k sorted lists, find min range which includes an element from each
# list of band performances what window of days to visit festival

import heapq as hq


def init_pq(arrays):
    pq = []
    maxInQ = float("-inf")

    for i, array in enumerate(arrays):
        if len(array) > 0:
            el = array[0]
            pq.append((el, i, 0))
            maxInQ = max(maxInQ, el)
        else:
            raise ValueError(f"array {i} is empty")

    hq.heapify(pq)
    return pq, maxInQ


def find_range(arrays):

    pq, maxInQ = init_pq(arrays)
    left = float("-inf")
    right = maxInQ

    while len(pq) == len(arrays):
        el, i, j = hq.heappop(pq)

        if right - left > maxInQ - el:
            left = el
            right = maxInQ

        if j + 1 < len(lists[i]):
            new_el = lists[i][j + 1]
            hq.heappush(pq, (new_el, i, j + 1))
            # maxInQ always incerases as the array is increasing
            maxInQ = max(maxInQ, new_el)

    return left, right


lists = [[5, 7, 13, 17, 21], [2, 4, 8, 16], [1, 10, 20]]
print(find_range(lists))

# given k sorted list, find min range so that atleast one el from each list is included
# list of band perfomances what window of days to visit festival

from queue import PriorityQueue


def init_pq(lists):
    pq = PriorityQueue()
    maxInQ = float("-inf")

    for i, l in enumerate(lists):
        if len(l) > 0:
            el = l[0]
            pq.put((el, i, 0))
            maxInQ = max(maxInQ, el)

    return pq, maxInQ


def find_range(lists):
    if any(filter(lambda l: len(l) == 0, lists)):
        raise ValueError("found empty list")

    pq, maxInQ = init_pq(lists)
    left = float("-inf")
    right = maxInQ

    while not pq.empty():
        el, i, j = pq.get()
        if right - left > maxInQ - el:
            right = maxInQ
            left = el

        if j + 1 < len(lists[i]):
            new_el = lists[i][j + 1]
            pq.put((new_el, i, j + 1))
            maxInQ = max(maxInQ, new_el)
        else:
            break

    return left, right


lists = [[5, 7, 13, 17], [2, 4, 8, 16], [1, 10, 20]]
print(find_range(lists))

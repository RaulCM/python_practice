import heapq


class RevCmp:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return not (self.value < other.value)


max_heap = list(map(RevCmp, "axuebizjmf"))
heapq.heapify(max_heap)

print(f"root = {max_heap[0].value}")

while len(max_heap) > 0:
    print(f"popped {heapq.heappop(max_heap).value}")

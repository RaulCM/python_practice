from queue import PriorityQueue
from collections import defaultdict
from pprint import pprint


def make_undir_wt_graph(edges):
    adj_list = defaultdict(list)
    for u, v, w in edges:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))

    return dict(adj_list)


def dijkstra(adj_list, src):
    distance = defaultdict(lambda: float("inf"))
    predecessor = dict()

    pq = PriorityQueue()
    pq.put((0, src))

    while not pq.empty():
        d, u = pq.get()
        if d <= distance[u]:
            distance[u] = d
            for v, w in adj_list[u]:
                d1 = d + w
                if d1 < distance[v]:
                    pq.put((d1, v))
                    predecessor[v] = u
                    distance[v] = d1

    return distance, predecessor


def get_path(src, dst, predecessor):
    path = []
    u = dst
    if u in predecessor or u == src:
        while u is not None:
            path.append(u)
            u = predecessor.get(u)

    return list(reversed(path))


edges = [
    (1, 2, 4),
    (1, 3, 4),
    (2, 3, 4),
    (3, 4, 3),
    (3, 5, 1),
    (3, 6, 6),
    (4, 6, 2),
    (5, 6, 3),
]

adj_list = make_undir_wt_graph(edges)
pprint(adj_list)

distance, predecessor = dijkstra(adj_list, 1)
pprint(distance)
pprint(get_path(1, 6, predecessor))

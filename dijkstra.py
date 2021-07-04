from queue import PriorityQueue


def make_undir_wt_graph(edges):
    adj_list = dict()
    for u, v, w in edges:
        adj_list.setdefault(u, []).append((v, w))
        adj_list.setdefault(v, []).append((u, w))

    return adj_list


def dijkstra(adj_list, src):
    distance = dict()
    predecessor = dict()
    visited = set()

    pq = PriorityQueue()
    pq.put((0, src))

    while not pq.empty():
        d, u = pq.get()
        if u not in visited:
            # since we dont have a decrease key op on Pq,
            # keep track of expanded vertices explicitly and ignore duplicates in Q
            distance[u] = d
            visited.add(u)

            for v, w in adj_list[u]:
                d1 = d + w
                if d1 < distance.get(v, float("inf")):
                    assert v not in visited
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
print("adj list", adj_list)

distance, predecessor = dijkstra(adj_list, 1)
print("distances from 1", distance)
print("path 1 to 6", get_path(1, 6, predecessor))

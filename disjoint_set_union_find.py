class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n


    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            x, y = y, x

        self.parent[y] = x

        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1


    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


    def count(self):
        s = {self.find(x) for x in range(len(self.parent))}
        return len(s)


#############


def count_connected_components(n, edges):
  dj = DisjointSet(n)

  for u, v in edges:
    dj.union(u, v)

  return dj.count()

count_connected_components(5, [[0, 1], [0, 2], [3, 4], [2, 3]])

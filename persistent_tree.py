
class Node:
    def __init__(self, k, v, lt = None, rt = None):
        self.key = k
        self.val = v
        self.left = lt
        self.right = rt


def put(node, k, v):
    if node is None:
        return Node(k, v)

    if k < node.key:
        return Node(node.key, node.val, put(node.left, k, v), node.right)
    elif k > node.key:
        return Node(node.key, node.val, node.left, put(node.right, k, v))
    else:
        return Node(k, v, node.left, node.right)


def get(node, k):
    if node is None:
        return None

    if k < node.key:
        return get(node.left, k)
    elif k > node.key:
        return get(node.right, k)
    else:
        return node.val

def contents(node):
    if node is None:
        return []

    acc = []
    if node.left:
        acc.append(contents(node.left))

    acc.append((node.key, node.val))

    if node.right:
        acc.append(contents(node.right))

    return acc




h1 = Node(1, 'a')
h2 = put(h1, 2, 'b')
h3 = put(h2, 3, 'c')
h4 = put(h2, 3, 'cc')

print(contents(h1))
print(contents(h2))
print(contents(h3))
print(contents(h4))

print(get(h1, 3))

print(get(h2, 1))
print(get(h2, 2))

print(get(h3, 3))
print(get(h4, 3))

h = None
for i in range(10):
    h = put(h, i, i * 10)

h = put(h, 5, 5)

print(contents(h))

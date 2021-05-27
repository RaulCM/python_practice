
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree(items):
    if items is None:
        return None
    
    left = make_tree(items[1])
    right = make_tree(items[2])

    return Node(items[0], left, right)


def levels(root):
    levels = []
    frontier = deque()

    frontier.append(root)

    while len(frontier) > 0:
        l = len(frontier)
        acc = []
        for _ in range(l):
            node = frontier.popleft()
            acc.append(node.val)
            if node.left:
                frontier.append(node.left)
            if node.right:
                frontier.append(node.right)
        
        levels.append(acc)

    return levels


def r_ht(root):
    if root is None:
        return 0
    
    h = 0
    node = root

    while node:
        h += 1
        node = node.right
    
    return h


def l_ht(root):
    if root is None:
        return 0
    
    h = 0
    node = root

    while node:
        h += 1
        node = node.left
    
    return h


def count_complete_tree(node):
    lh = l_ht(node)
    rh = r_ht(node)

    if lh == rh:
        # tree is full
        return (2 ** lh) - 1
    else:
        return 1 + count_complete_tree(node.left) + count_complete_tree(node.right)


def find_node_by_pos(root, i):
    """1 based level wise indexing like heap"""
    if i < 1:
        return None
    if i == 1:
        return root
    
    stack = []

    while i > 1:
        if i % 2 == 1:
            stack.append('r')
        else:
            stack.append('l')
        i = i // 2    

    node = root
    for op in reversed(stack):
        if op == 'l':
            node = node.left
        else:
            node = node.right

    return node


def find_vaccant_node(root):
    # finds node where child can be inserted preserving left completeness
    count = count_complete_tree(root)
    i = (count + 1) // 2
    node = find_node_by_pos(root, i)
    return node


def insert_complete_tree(root, val):
    # inserts val preserving left completeness
    node = Node(val)
    if not root:
        return node
    
    parent = find_vaccant_node(root)
    if parent.left is None:
        parent.left = node
    else:
        parent.right = node

    return root


def inorder_gen(root):
    if root:
        yield from inorder_gen(root.left)
        yield root.val
        yield from inorder_gen(root.right)


items = [1, [2, [4, None, None], [5, None, None]], [3, [6, None, None], None]]
# items = [1,  [2,None, None], None]

root = make_tree(items)

# print("levels", levels(root))
# print("l_ht", l_ht(root))
# print("r_ht", r_ht(root))
# print("count_complete_tree", count_complete_tree(root))

# for i in range(1, 8):
#     print(f"{i}", find_node_by_pos(root, i).val)

# print("find_vaccant_node", find_vaccant_node(root).val)

insert_complete_tree(root, 7)
print("levels", levels(root))


for it in inorder_gen(root):
    print(it)

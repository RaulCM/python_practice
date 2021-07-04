def count(node, target):
    """ counts occurrences of target in node's hierarchy"""
    if node == target:
        return 1

    if isinstance(node, list):
        return sum(count(el, target) for el in node)

    if isinstance(node, dict):
        return sum(count(el, target) for el in node.values())

    return 0


def path_to(target, node):
    """subscript path to target inside node's hierarchy"""
    if node == target:
        return f" -> {target!r}"
    elif isinstance(node, list):
        for i, el in enumerate(node):
            path = path_to(target, el)
            if path:
                return f"[{i}]{path}"
    elif isinstance(node, dict):
        for key, el in node.items():
            path = path_to(target, el)
            if path:
                return f"[{key!r}]{path}"

    return None

print(path_to("a1", ["a", "b", ["a", {"x" : "a1"}]]))
print(count(["a", "b", ["a", {"x" : "a"}]], "a"))

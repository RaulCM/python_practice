# flatten nested array [[1, [2, [3]]], 4] -> [1,2,3,4]


def flatten(input):
    if input is None:
        return None

    acc = []

    for el in input:
        if isinstance(el, list):
            acc.extend(flatten(el))
        else:
            acc.append(el)

    return acc


print(flatten([[1, [2, [3]]], 4]))

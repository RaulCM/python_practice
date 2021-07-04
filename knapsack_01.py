from collections import defaultdict


def knapsack_01_recur(weights, values, capacity):
    def recur(i, weight_so_far, value_so_far, memo):
        if i == len(weights):
            return value_so_far

        if (i, weight_so_far) in memo:
            return memo[(i, weight_so_far)]

        ans = 0
        if weights[i] + weight_so_far <= capacity:
            ans = recur(
                i + 1,
                weight_so_far + weights[i],
                value_so_far + values[i],
                memo,
            )

        ans = max(
            ans,
            recur(i + 1, weight_so_far, value_so_far, memo),
        )

        memo[(i, weight_so_far)] = ans
        return ans

    return recur(0, 0, 0, {})


def knapsack_01(weights, values, capacity):
    assert len(weights) == len(values), f"{weights} and {values} unequal"
    gains = defaultdict(int)
    selection = defaultdict(int)

    for i, (wi, vi) in enumerate(zip(weights, values)):

        for w in range(1, capacity + 1):
            if wi <= w and vi + gains[(i - 1, w - wi)] > gains[(i - 1, w)]:
                gains[(i, w)] = vi + gains[(i - 1, w - wi)]
                selection[(i, w)] = 1
            else:
                gains[(i, w)] = gains[(i - 1, w)]
                selection[(i, w)] = 0

    current = capacity
    ans = []
    for i in reversed(range(len(weights))):
        if selection[(i, current)] == 1:
            ans.append((weights[i], values[i]))
            current -= weights[i]

    return ans


weights = [5, 4, 6, 3]
values = [10, 40, 30, 60]
capacity = 10

print(knapsack_01(weights, values, capacity))
print(knapsack_01_recur(weights, values, capacity))

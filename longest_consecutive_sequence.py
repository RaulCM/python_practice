
def explore(x, unvisited):
    left = x - 1
    while left in unvisited:
        unvisited.remove(left)
        left -= 1
    left += 1

    right = x + 1
    while right in unvisited:
        unvisited.remove(right)
        right += 1
    right -= 1

    return (left, right)


def longestConsecutiveSequence(nums):
    unvisited = set(nums)

    longest = -1
    ans = None

    for i, x in enumerate(nums):
        if x not in unvisited:
            # already explored
            continue

        unvisited.remove(x)
        left, right = explore(x, unvisited)

        if right - left > longest:
            longest = right - left
            ans = (left, right)

    return ans


print(longestConsecutiveSequence([97, 5, 2, 99, 3, 4, 1, 100]))

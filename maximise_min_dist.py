
def can_place(spots, k, dist):
    last = spots[0]
    remaining = k - 1

    for current in spots[1:]:
        if current - last >= dist:
            last = current
            remaining -= 1
            if remaining == 0:
                return True

    return False


def maximise_min_dist(spots, k):
    """place k items in spots such that min dist between them is maximized"""

    spots.sort()

    ans = -1

    left = spots[0]
    right = spots[-1] - left

    while left < right:
        mid = left + (right - left + 1) // 2

        if can_place(spots, k, mid):
            ans = max(ans, mid)
            left = mid + 1
        else:
            right = mid - 1

    return ans



print(maximise_min_dist([1, 2, 8, 4, 9], 3))
print(maximise_min_dist([1, 2, 7, 5, 11, 12], 3))

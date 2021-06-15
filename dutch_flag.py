# partition 3 way using a classifier returning 0, 1, 2
import random


def three_way_partition(items, classifier):
    # divide into 4 sec, unknown region is shrunk while maintaining these conditions
    # 0->lo-1 => 0s
    # lo->mid-1 => 1s
    # mid->hi => unknown
    # hi+1->end-1 => 2s
    #             |
    # 0 0 0 1 1 1 ? ? ? ? 2 2 2
    #       ^     ^     ^
    #       |     |     |
    #       Lo    Mid   Hi

    lo = 0
    mid = 0
    hi = len(items) - 1

    while mid <= hi:
        mapped = classifier(items[mid])
        if mapped == 0:
            items[lo], items[mid] = items[mid], items[lo]
            lo += 1
            mid += 1
        elif mapped == 1:
            mid += 1
        elif mapped == 2:
            items[mid], items[hi] = items[hi], items[mid]
            hi -= 1
        else:
            raise ValueError(f"Got {mapped} for {items[mid]} in pos {mid}")


items = list(range(10))
three_way_partition(items, lambda x: x % 3)
print(items)

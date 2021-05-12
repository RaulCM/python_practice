import itertools
import heapq


def kth_largest_product(nums1, nums2, k):
    """find kth largest product of any 2 items from each list"""
    nums2.sort()

    def gen_asc(i):
        return (nums1[i] * y for y in nums2)

    def gen_desc(i):
        return (nums1[i] * y for y in reversed(nums2))

    items = (gen_desc(i) if x > 0 else gen_asc(i) for i, x in enumerate(nums1))
    it = heapq.merge(*items, reverse=True)
    return next(itertools.islice(it, k, k+1))


print(kth_largest_product([-2, 4, 3], [5, 7], 2))
print(kth_largest_product([-3, -2, -1], [3, 2, 1], 1))
print(kth_largest_product([-3, 0], [3, -2, 1], 1))

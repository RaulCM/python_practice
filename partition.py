def partition(nums, start, end, predicate):
    # array is [start,end] inclusive;
    # Invariant: [start, lo-1] are all zero, [hi+1, end] are all one, [lo,hi] are unknown.
    lo = start
    hi = end

    while lo <= hi:
        if predicate(nums[lo]):
            lo += 1
        else:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            hi -= 1

    return lo


nums = [0, 1, 2, 0, 1, 2]

pivot = partition(nums, 0, len(nums) - 1, lambda x: x == 0)
print(nums, pivot)

pivot = partition(nums, 2, len(nums) - 1, lambda x: x == 1)
print(nums, pivot)

nums = [2, 1, 0, 2, 1, 0]

pivot = partition(nums, 0, len(nums) - 1, lambda x: x == 0)
print(nums, pivot)

pivot = partition(nums, 2, len(nums) - 1, lambda x: x == 1)
print(nums, pivot)

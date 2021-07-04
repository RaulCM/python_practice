# return the lexicographically smallest subsequence of length k.

def fix_stack(i, x, stack, k, n):
    unused = n - 1 - i
    while len(stack) > 0 and x < stack[-1] and (len(stack) + unused) >= k:
        stack.pop()

def find_smallest_subseq(nums, k):
    if k <= 0:
        return []

    n = len(nums)
    stack = []

    for i, x in enumerate(nums):
        fix_stack(i, x, stack, k, n)
        stack.append(x)

    return stack[:k]



nums = [10, 1, 0]
k = 2
print(find_smallest_subseq(nums, k))

nums = [1, 2, 0, 9, 2, 3]
k = 3
print(find_smallest_subseq(nums, k))

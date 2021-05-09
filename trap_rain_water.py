def trapped_water_vol(heights):
    """instead of calculating area by height*width, 
    we can consider it in a cumulative way. 
    sum water amount of each bin( of width=1).
    
    Search from left to right and maintain a max height of left and right separately,
     which is like a one-side wall of partial container.
    
    Fix the higher one and flow water from the lower part.

    For example,
    if current height of left is lower, we fill water in the left bin.
    Until left meets right, we filled the whole container."""


    n = len(heights)

    left = 0
    right = n - 1

    res = 0

    maxLeft = maxRight = 0

    while left <= right:
        if heights[left] <= heights[right]:
            if heights[left] >= maxLeft:
                maxLeft = heights[left]
            else:
                res += maxLeft - heights[left]

            left += 1
        else:
            if heights[right] >= maxRight:
                maxRight = heights[right]
            else:
                res += maxRight - heights[right]

            right -= 1

    return res


def trapped_water_vol_1(heights):
    """3 passes :
    find tallest tower pos
    from left to tallest pos, accumulate water
    from right to tallest pos, accumulate water
    """

    n = len(heights)

    if n < 3:
        return 0

    tallest_pos = 0

    for i in range(n):
        if heights[i] > heights[tallest_pos]:
            tallest_pos = i

    water = 0

    left_barrier = 0
    for i in range(tallest_pos):
        if left_barrier < heights[i]:
            left_barrier = heights[i]
        else:
            water += left_barrier - heights[i]

    right_barrier = 0
    for i in reversed(range(tallest_pos + 1, n)):
        if right_barrier < heights[i]:
            right_barrier = heights[i]
        else:
            water += right_barrier - heights[i]

    return water


print(trapped_water_vol([4,2,0,3,2,5]))
print(trapped_water_vol_1([4,2,0,3,2,5]))

print(trapped_water_vol([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trapped_water_vol_1([0,1,0,2,1,0,1,3,2,1,2,1]))

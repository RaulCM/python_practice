
def spiral_matrix(matrix):

    if len(matrix) < 1:
        return []

    acc = []
    direction = 0

    top = 0
    bottom = len(matrix)
    left = 0
    right = len(matrix[0])

    while left <= right and top <= bottom:

        if direction == 0:
            for i in range(left, right):
                acc.append(matrix[top][i])
            top += 1

        if direction == 1:
            for i in range(top, bottom):
                acc.append(matrix[i][right])
            right -= 1

        if direction == 2:
            for i in reversed(range(left, right)):
                acc.append(matrix[bottom][i])
            bottom -= 1

        if direction == 3:
            for i in reversed(range(bottom, top)):
                acc.append(matrix[i][left])
            left += 1

    return acc


 
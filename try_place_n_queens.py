def can_place(i, j, queens):
    for x,y in queens:
        if i == x or j == y or i + j == x + y or i - j == x - y:
            return False

    return True


def find_queens(board, n):
    queens = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                queens.append((i,j))

    return queens


def find_next(queens, n):
    rows = {r for r,c in queens}
    for i in range(n):
        if i not in rows:
            return i


def try_place(n, queens):
    if len(queens) == n:
        print(queens)
        return True

    i = find_next(queens, n)

    for j in range(n):
        if can_place(i, j, queens):
            if try_place(n, queens + [(i, j)]):
                return True

    return False


def can_solve(board):
    """given initial board, can we solve n queens"""
    n = len(board)
    if n == 3 or n == 2:
        return False

    queens = find_queens(board, n)
    if len(queens) < 3:
        return True

    return try_place(n, queens)


print(
    can_solve([
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
    ])
)


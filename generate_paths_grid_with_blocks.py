# starting from top left go to bottom right in grid, only taking right or down moves
# some cells are blocked, only pass through cells having 0


def gen_paths(r, c, grid, dest_r, dest_c, path_so_far, all_paths):
    if (r, c) == (dest_r, dest_c):
        all_paths.append(path_so_far)
        return

    if grid[r][c] != "0":
        return

    if r < dest_r:
        gen_paths(r + 1, c, grid, dest_r, dest_c, path_so_far + ["D"], all_paths)

    if c < dest_c:
        gen_paths(r, c + 1, grid, dest_r, dest_c, path_so_far + ["R"], all_paths)


no_way_grid = """
0000
1110
0000
0111
0000
""".split()

grid = """
00000
11101
00000
01110
00000
""".split()

acc = []
gen_paths(0, 0, no_way_grid, 4, 3, [], acc)
print(acc)

acc = []
gen_paths(0, 0, grid, 4, 4, [], acc)
print(acc)

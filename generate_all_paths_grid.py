# starting from top left go to bottom right in grid, only taking right or down moves


def gen_paths(r, c, dest_r, dest_c, path_so_far, all_paths):
    if (r, c) == (dest_r, dest_c):
        all_paths.append(path_so_far)
        return

    if r < dest_r:
        gen_paths(r + 1, c, dest_r, dest_c, path_so_far + ["D"], all_paths)

    if c < dest_c:
        gen_paths(r, c + 1, dest_r, dest_c, path_so_far + ["R"], all_paths)


acc = []
gen_paths(0, 0, 2, 3, [], acc)
print(acc)

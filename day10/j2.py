import numpy as np

with open("input.txt") as f:
    lines = [[int(c) for c in l.strip("\n")] for l in f.readlines()]

lava_map = np.array(lines)


def in_bound(pos):
    return (
        pos[0] >= 0
        and pos[1] >= 0
        and pos[1] < lava_map.shape[0]
        and pos[0] < lava_map.shape[1]
    )


seed = zip(*np.where(lava_map == 0))
level = 0

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
trail_paths = 0
for s in seed:
    cur_level = set([s])
    for level in range(1, 10):
        next_level = set()
        for x, y in cur_level:
            for dx, dy in direction:
                new_pos = x + dx, y + dy
                if in_bound(new_pos) and lava_map[new_pos] == level:
                    next_level.add(new_pos)
        cur_level = next_level
    trail_paths += len(cur_level)

print(trail_paths)

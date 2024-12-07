import numpy as np
import time

t0 = time.time()

with open("input.txt") as f:
    lines = [[c for c in l.strip("\n")] for l in f.readlines()]

guard_map = np.array(lines)
guard_map_shape = guard_map.shape

move_direction = {0: (-1, 0), 3: (0, -1), 2: (1, 0), 1: (0, 1)}

a, b = np.where(guard_map == "^")
starting_pos = a[0], b[0]


def traversial(map, starting_pos, first_try=True):
    current_direction = 0
    pos = starting_pos

    pos_dir = set()
    pos_dir.add((pos[0], pos[1], current_direction))
    status = "exited"
    obstacles = set([(int(x), int(y)) for x, y in zip(*np.where(map == "#"))])
    while True:
        if first_try:
            map[pos] = "X"
        move = move_direction[current_direction]
        next_pos = pos[0] + move[0], pos[1] + move[1]
        if (
            next_pos[0] < 0
            or next_pos[1] < 0
            or next_pos[1] >= guard_map_shape[0]
            or next_pos[0] >= guard_map_shape[1]
        ):
            break
        cpt = 0
        dir_change = False
        while next_pos in obstacles:
            dir_change = True
            current_direction = (current_direction + 1) % 4
            move = move_direction[current_direction]
            next_pos = pos[0] + move[0], pos[1] + move[1]
            cpt += 1
        pos = next_pos
        if dir_change:
            cur_pos_dir = (pos[0], pos[1], current_direction)
            if cur_pos_dir in pos_dir:
                status = "loop"
                break
            pos_dir.add(cur_pos_dir)

    return map, status


original_traversial, _ = traversial(guard_map, starting_pos)
ii, jj = np.where(original_traversial == "X")
print(len(ii))  # part 1


loop_count = 0
for idx in range(len(ii)):
    i, j = ii[idx], jj[idx]
    if i == starting_pos[0] and j == starting_pos[1]:
        continue
    new_map = guard_map.copy()
    new_map[i, j] = "#"
    result_map, status = traversial(new_map, starting_pos, False)
    if status == "loop":
        loop_count += 1

print(loop_count)
print(time.time() - t0)  # 64s -> 14s -> 5.7s

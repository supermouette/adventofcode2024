import numpy as np
import time

t0 = time.time()

with open("input.txt") as f:
    lines = [[c for c in l.strip("\n")] for l in f.readlines()]

guard_map = np.array(lines)

move_direction = {"up": (-1, 0), "left": (0, -1), "down": (1, 0), "right": (0, 1)}
directions = ["up", "right", "down", "left"]

a, b = np.where(guard_map == "^")
starting_pos = a[0], b[0]


def in_bound(pos):
    return (
        pos[0] >= 0
        and pos[1] >= 0
        and pos[1] < guard_map.shape[0]
        and pos[0] < guard_map.shape[1]
    )


def traversial(map, starting_pos):
    current_direction = 0
    pos = starting_pos

    pos_dir = set()
    pos_dir.add((pos[0], pos[1], current_direction))
    status = "exited"
    while True:
        map[pos] = "X"
        move = move_direction[directions[current_direction]]
        next_pos = pos[0] + move[0], pos[1] + move[1]
        if not in_bound(next_pos):
            break
        cpt = 0
        while map[next_pos] == "#":
            current_direction = (current_direction + 1) % 4
            move = move_direction[directions[current_direction]]
            next_pos = pos[0] + move[0], pos[1] + move[1]
            cpt += 1
            if cpt > 10:
                print(pos)
                print(map)
                print("huuuu")
                exit()
        pos = next_pos
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
    result_map, status = traversial(new_map, starting_pos)
    if status == "loop":
        loop_count += 1

print(loop_count)
print(time.time() - t0)  # 64s -> 14s

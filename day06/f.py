import numpy as np

with open("input.txt") as f:
    lines = [[c for c in l.strip("\n")] for l in f.readlines()]

guard_map = np.array(lines)

move_direction = {"up": (-1, 0), "left": (0, -1), "down": (1, 0), "right": (0, 1)}
directions = ["up", "right", "down", "left"]
current_direction = 0

a, b = np.where(guard_map == "^")
pos = a[0], b[0]


def in_bound(pos):
    return (
        pos[0] >= 0
        and pos[1] >= 0
        and pos[1] < guard_map.shape[0]
        and pos[0] < guard_map.shape[1]
    )


while True:
    guard_map[pos] = "X"
    move = move_direction[directions[current_direction]]
    next_pos = pos[0] + move[0], pos[1] + move[1]
    if not in_bound(next_pos):
        break
    while guard_map[next_pos] == "#":
        current_direction = (current_direction + 1) % 4
        move = move_direction[directions[current_direction]]
        next_pos = pos[0] + move[0], pos[1] + move[1]
    pos = next_pos

print(np.count_nonzero(guard_map == "X"))

import numpy as np
import matplotlib.pyplot as plt

with open("input.txt") as f:
    lines = f.readlines()


robots = []

for l in lines:
    robots.append(
        [[int(c) for c in s[2:].split(",")] for s in l.strip("\n").split(" ")]
    )

map_size = [7, 11] if len(lines) < 20 else [103, 101]
step = 100


def move_robots(step, safety_check=False):
    final_map = np.zeros(map_size, dtype=int)
    for robot in robots:
        (y, x), (dy, dx) = robot
        new_x, new_y = (x + step * dx) % map_size[0], (y + step * dy) % map_size[1]
        if new_x < 0:
            new_x += map_size[0]
        if new_y < 0:
            new_y += map_size[1]
        final_map[(new_x, new_y)] += 1

    if safety_check:
        safety_factor = (
            sum(sum(final_map[: map_size[0] // 2, : map_size[1] // 2]))
            * sum(sum(final_map[map_size[0] // 2 + 1 :, : map_size[1] // 2]))
            * sum(sum(final_map[: map_size[0] // 2, map_size[1] // 2 + 1 :]))
            * sum(sum(final_map[map_size[0] // 2 + 1 :, map_size[1] // 2 + 1 :]))
        )
    else:
        safety_factor = 0
    return final_map, safety_factor


print(move_robots(100, True))

# kind of cheated, saw that post earlier today : https://www.reddit.com/r/adventofcode/comments/1hefkyo/2024_day_14_part_2_i_found_it_showing_all/
# There is some kind of repeated pattern, as robots are always moving the same + there is a fixed length map.

"""
for i in range(map_size[0]):
    print(i)
    io.imshow(move_robots(i)[0])
    io.show()
"""
# 23, 49 are weird looking

for i in range(60, map_size[1]):
    print("---", i)
    print(i * 103 + 23)  # => that's the one, at i=63, 6512
    plt.imshow(move_robots(i * 103 + 23)[0])
    plt.show()

    print(i * 103 + 49)
    plt.imshow(move_robots(i * 103 + 43)[0])
    plt.show()

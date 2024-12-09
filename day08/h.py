import numpy as np

with open("input.txt") as f:
    lines = [[c for c in l.strip("\n")] for l in f.readlines()]

antenas = {}


def in_bound(pos):
    i, j = pos
    return i >= 0 and j >= 0 and j < len(lines[0]) and i < len(lines)


for i in range(len(lines)):
    for j in range(len(lines[0])):
        location = lines[i][j]
        if location != ".":
            antenas[location] = antenas.get(location, []) + [(i, j)]

antinodes = set()

for frequency in antenas.keys():
    for x, (i1, j1) in enumerate(antenas[frequency][:-1]):
        for i2, j2 in antenas[frequency][x + 1 :]:
            di, dj = i2 - i1, j2 - j1
            a1 = (i1 - di, j1 - dj)
            a2 = (i2 + di, j2 + dj)
            if in_bound(a1):
                antinodes.add(a1)
            if in_bound(a2):
                antinodes.add(a2)
"""
for i, j in antinodes:
    lines[i][j] = "#"
for l in lines:
    print("".join(l))
"""

print(len(antinodes))  # part 1

antinodes = set()

for frequency in antenas.keys():
    for x, (i1, j1) in enumerate(antenas[frequency][:-1]):
        for i2, j2 in antenas[frequency][x + 1 :]:
            di, dj = i2 - i1, j2 - j1
            a1 = i1, j1
            factor = 0
            while in_bound(a1):
                antinodes.add(a1)
                factor += 1
                a1 = (i1 - factor * di, j1 - factor * dj)
            a2 = i2, j2
            factor = 0
            while in_bound(a2):
                antinodes.add(a2)
                factor += 1
                a2 = (i2 + factor * di, j2 + factor * dj)

"""
for i, j in antinodes:
    lines[i][j] = "#"
for l in lines:
    print("".join(l))
"""

print(len(antinodes))  # part 2

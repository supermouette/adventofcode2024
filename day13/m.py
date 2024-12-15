import numpy as np


with open("input.txt") as f:
    lines = [l.strip("\n") for l in f.readlines()]

prize = 0
for i in range(len(lines) // 4 + 1):
    extract = lines[i * 4 : i * 4 + 3]
    ax, ay = [int(c[2:]) for c in extract[0][len("Button A: ") :].split(", ")]
    bx, by = [int(c[2:]) for c in extract[1][len("Button B: ") :].split(", ")]
    px, py = [int(c[2:]) for c in extract[2][len("Prize: ") :].split(", ")]

    a, b = np.linalg.solve(np.array([[ax, bx], [ay, by]]), np.array([px, py]))
    a = int(round(a))
    b = int(round(b))
    if px == ax * a + bx * b and py == ay * a + by * b and a <= 100 and b <= 100:
        prize += a * 3 + b

print(prize)

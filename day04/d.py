with open("input.txt") as f:
    lines = [l.strip("\n") for l in f.readlines()]

# if you read this, please take in account that I'm sick, and this is 6am... well, now 7am :'(

xmas_counter = 0
l, w = len(lines), len(lines[0])
# horizontal
for line in lines:
    xmas_counter += line.count("XMAS")
    xmas_counter += line.count("SAMX")

# vertical
for j in range(w):
    v_line = "".join([lines[i][j] for i in range(l)])
    xmas_counter += v_line.count("XMAS")
    xmas_counter += v_line.count("SAMX")


# diagonal
"""
AZER
AZER
AZER

=>
[(0, 0)]
[(0, 1), (1, 0)]
[(0, 2), (1, 1), (2, 0)]
[(1, 2), (2, 2), (2, 1), (3, 0)]
...

[(0, 3)]
[(0, 2), (1, 3)]
[(0, 1), (1, 2), (2, 3)]
"""

for diag in range(l):
    diag_line = ""
    diag_idx = []
    for i in range(diag + 1):
        diag_idx.append((i, diag - i))
        diag_line += lines[i][diag - i]
    # print(diag_idx)
    # print(diag_line)
    xmas_counter += diag_line.count("XMAS")
    xmas_counter += diag_line.count("SAMX")


for diag in range(w - 2, -1, -1):
    diag_line = ""
    diag_idx = []
    for i in range(diag + 1):
        diag_idx.append((l - 1 + i - diag, w - 1 - i))
        diag_line += lines[l - 1 + i - diag][w - 1 - i]
    # print(diag_idx)
    # print(diag_line)
    xmas_counter += diag_line.count("XMAS")
    xmas_counter += diag_line.count("SAMX")


for diag in range(l):
    diag_line = ""
    diag_idx = []
    for i in range(diag + 1):
        diag_idx.append((i, i + w - 1 - diag))
        diag_line += lines[i][i + w - 1 - diag]
    # print(diag_idx)
    # print(diag_line)
    xmas_counter += diag_line.count("XMAS")
    xmas_counter += diag_line.count("SAMX")

for diag in range(w - 2, -1, -1):
    diag_line = ""
    diag_idx = []
    for i in range(diag + 1):
        diag_idx.append((i + w - 1 - diag, i))
        diag_line += lines[i + w - 1 - diag][i]
    # print(diag_idx)
    # print(diag_line)
    xmas_counter += diag_line.count("XMAS")
    xmas_counter += diag_line.count("SAMX")

print(xmas_counter)  # part 1

"""
patterns :
M.S M.M S.S S.M
.A. .A. .A. .A.
M.S S.S M.M S.M
"""


def find_xmas(s):
    return (
        (
            s[0][0] == "M"
            and s[0][2] == "S"
            and s[1][1] == "A"
            and s[2][0] == "M"
            and s[2][2] == "S"
        )
        or (
            s[0][0] == "M"
            and s[0][2] == "M"
            and s[1][1] == "A"
            and s[2][0] == "S"
            and s[2][2] == "S"
        )
        or (
            s[0][0] == "S"
            and s[0][2] == "S"
            and s[1][1] == "A"
            and s[2][0] == "M"
            and s[2][2] == "M"
        )
        or (
            s[0][0] == "S"
            and s[0][2] == "M"
            and s[1][1] == "A"
            and s[2][0] == "S"
            and s[2][2] == "M"
        )
    )


xmas_counter = 0
for i in range(l - 2):
    for j in range(w - 2):
        patch = lines[i][j : j + 3], lines[i + 1][j : j + 3], lines[i + 2][j : j + 3]
        if find_xmas(patch):
            xmas_counter += 1
print(xmas_counter)

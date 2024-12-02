with open("input.txt") as f:
    lines = [
        (i, True, [int(s) for s in l.strip("\n").split(" ")])
        for i, l in enumerate(f.readlines())
    ]


safe = 0
# part 1
for _, _, l in lines:
    if l[0] == l[1]:
        continue
    sign_l = (l[0] - l[1]) / abs(l[0] - l[1])
    for i in range(1, len(l)):
        if l[i] == l[i - 1]:
            break
        sign_i = (l[i - 1] - l[i]) / abs(l[i - 1] - l[i])
        if sign_l == sign_i and 1 <= abs(l[i - 1] - l[i]) <= 3:
            continue
        else:
            break
    else:
        safe += 1

print(safe)

# part 2


def all(idx, l):
    res = []
    for i in range(len(l) - 1):
        res.append((idx, False, l[:i] + l[i + 1 :]))
    res.append((idx, False, l[:-1]))
    return res


safe = set()
for idx, can_retry, l in lines:
    if l[0] == l[1]:
        if can_retry:
            for l2 in all(idx, l):
                lines.append(l2)
        continue
    sign_l = (l[0] - l[1]) / abs(l[0] - l[1])
    for i in range(1, len(l)):
        if l[i] == l[i - 1]:
            if can_retry:
                for l2 in all(idx, l):
                    lines.append(l2)
            break
        sign_i = (l[i - 1] - l[i]) / abs(l[i - 1] - l[i])
        if sign_l == sign_i and 1 <= abs(l[i - 1] - l[i]) <= 3:
            continue
        else:
            if can_retry:
                for l2 in all(idx, l):
                    lines.append(l2)
            break
    else:
        safe.add(idx)
print(len(safe))

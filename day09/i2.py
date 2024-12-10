with open("input.txt") as f:
    line = f.readline().strip("\n")

# line = "2333133121414131402"  # example


is_file = True
mem = []

for i in range(len(line)):
    length = int(line[i])
    for x in range(length):
        mem.append(str(i // 2) if is_file else ".")
    is_file = not is_file

# print("".join(mem))

i = len(mem) - 1

while i > 0:
    i0 = i
    span = 1
    while mem[i - 1] == mem[i0]:
        span += 1
        i -= 1
    if mem[i0] == ".":
        i -= 1
        continue

    # search for empty space
    empty_span = 0
    for j in range(len(mem[:i])):
        if mem[j] != ".":
            empty_span = 0
        else:
            empty_span += 1
            if empty_span == span:
                for k in range(span):
                    mem[j - empty_span + k + 1] = mem[i0]
                    mem[i + k] = "."
                break
    i -= 1

# print("".join(mem))
checksum = 0
for i, id in enumerate(mem):
    if id != ".":
        checksum += i * int(id)
print(checksum)

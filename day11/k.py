with open("input.txt") as f:
    stones = f.read().strip().split()

max_step = 25

stones = [int(s) for s in stones]
stone_len = [len(stones)]
for step in range(max_step):
    new_stones = []
    for stone in stones:
        ston_str = str(stone)
        if stone == 0:
            new_stones.append(1)
        elif len(ston_str) % 2 == 0:
            half = len(ston_str) // 2
            new_stones.append(int(ston_str[:half]))
            new_stones.append(int(ston_str[half:]))
        else:
            new_stones.append(stone * 2024)
    stones = new_stones
    stone_len.append(len(stones))


print(len(stones))

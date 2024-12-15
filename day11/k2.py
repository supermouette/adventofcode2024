from time import time
from functools import lru_cache

with open("input.txt") as f:
    stones = f.read().strip().split()

t0 = time()

max_step = 75

stones = [int(s) for s in stones]


@lru_cache(maxsize=None)
def compute(arr, step):
    if step == 0:
        return len(arr)
    arr_len = 0
    for i in arr:
        if i == 0:
            arr_len += compute((1,), step - 1)
        else:
            i_str = str(i)
            if len(i_str) % 2 == 0:
                half = len(i_str) // 2
                arr_len += compute((int(i_str[:half]),), step - 1)
                arr_len += compute((int(i_str[half:]),), step - 1)
            else:
                arr_len += compute((i * 2024,), step - 1)
    return arr_len


t0 = time()
print(compute(tuple(stones), max_step))
print(time() - t0)

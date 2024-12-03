import re

with open("input.txt") as f:
    memory = f.read()

mul_instr = re.findall("mul\((\d{1,3}),(\d{1,3})\)", memory)

print(sum([int(a) * int(b) for a, b in mul_instr]))  # part 1

instr_list = re.findall("mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", memory)

can, res = True, 0

for a, b, do, dont in instr_list:
    if do:
        can = True
    elif dont:
        can = False
    else:
        if can:
            res += int(a) * int(b)

print(res)  # part 2

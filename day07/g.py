from itertools import product

with open("input.txt") as f:
    lines = f.readlines()


def main_loop(operators):
    cpt = 0
    for l in lines:
        total, nbs = l.strip("\n").split(":")
        total = int(total)
        nbs = [int(nb) for nb in nbs.split()]
        for seed in product(operators, repeat=len(nbs) - 1):
            current_sum = nbs[0]
            for i, nb in enumerate(nbs[1:]):
                if seed[i] == "+":
                    current_sum += nb
                elif seed[i] == "*":
                    current_sum *= nb
                else:
                    current_sum = int(str(current_sum) + str(nb))
                if current_sum > total:
                    break
            if current_sum == total:
                cpt += total
                break
    return cpt


print(main_loop("+*"))
print(main_loop("+*|"))

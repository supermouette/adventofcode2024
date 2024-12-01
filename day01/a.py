with open("input.txt") as f:
    lines = [[int(s) for s in l.strip("\n").split("   ")] for l in f.readlines()]

list_1 = [l[0] for l in lines]
list_2 = [l[1] for l in lines]

list_1.sort()
list_2.sort()

distances = 0
histogram = {}
for i in range(len(list_1)):
    l1 = list_1[i]
    l2 = list_2[i]

    distances += abs(l1 - l2)

    histogram[l2] = histogram.get(l2, 0) + 1

print(distances)  # part 1

similarity = 0
for key in list_1:
    similarity += key * histogram.get(key, 0)
print(similarity)

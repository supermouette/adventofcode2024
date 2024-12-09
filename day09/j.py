with open("input.txt") as f:
    line = f.readline().strip("\n")

# line = "2333133121414131402"  # example

# print(line)

checksum = 0
id = {}
free_spaces = []

is_file = True
file_id_i = 0
i = 0
j = len(line) - 1
offset = 0
left_over = {}

debug = ""
while True:
    if is_file:
        if i > j:
            break
        length = int(line[i])
        if j == i:
            length = left_over[file_id_i]

        for x in range(length):
            checksum += file_id_i * offset
            offset += 1
        if j == i:
            break
        i += 1
        file_id_i += 1
        is_file = False
    else:
        length_free_space = int(line[i])
        while length_free_space != 0:
            length_file = int(line[j])
            if j // 2 not in left_over:
                left_over[j // 2] = length_file
            checksum += (j // 2) * offset
            offset += 1
            length_free_space -= 1
            left_over[j // 2] -= 1

            if left_over[j // 2] == 0:
                j -= 2
                while line[j] == "0":
                    j -= 2
        i += 1
        is_file = True

print(checksum)

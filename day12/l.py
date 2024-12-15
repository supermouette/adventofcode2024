from typing import List
import numpy as np
from skimage import io, measure, transform
import matplotlib.pyplot as plt

with open("input.txt") as f:
    farm = [[ord(c) - ord("A") for c in l.strip("\n")] for l in f.readlines()]

farm = np.array(farm)


def in_bound(pos):
    return (
        pos[0] >= 0
        and pos[1] >= 0
        and pos[1] < farm.shape[0]
        and pos[0] < farm.shape[1]
    )


direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]


label_img = measure.label(farm, connectivity=1, background=255)
regions: List[measure._regionprops.RegionProperties] = measure.regionprops(label_img)


p1 = 0
p2 = 0
for r in regions:
    area = r.num_pixels
    color = farm[r.coords[0][0], r.coords[0][1]]
    id = label_img[r.coords[0][0], r.coords[0][1]]
    perimeter = 0
    minr, minc, maxr, maxc = r.bbox
    patch = label_img[minr:maxr, minc:maxc].copy()
    patch[patch != id] = 0

    patch = np.c_[patch, np.zeros(patch.shape[0], dtype=np.uint8)]
    patch = np.c_[np.zeros(patch.shape[0], dtype=np.uint8), patch]
    patch = np.r_[patch, [np.zeros(patch.shape[1], dtype=np.uint8)]]
    patch = np.r_[[np.zeros(patch.shape[1], dtype=np.uint8)], patch]

    patch = patch.repeat(2, axis=0).repeat(2, axis=1)

    # io.imshow(patch)
    # io.show()

    contours = measure.find_contours(patch)

    corner_count = 0
    for contour in contours:
        prev = contour[0]
        for c in contour[1:]:
            if prev[0] != c[0] and prev[1] != c[1]:
                corner_count += 1
            prev = c[:]
    print(corner_count)
    """
    fig, ax = plt.subplots()
    ax.imshow(patch, cmap=plt.cm.gray)
    for c in contours:
        ax.plot(c[:, 1], c[:, 0], linewidth=2)
    ax.axis("image")
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()
    """

    for i, j in r.coords:
        for di, dj in direction:
            new_pos = i + di, j + dj
            if not in_bound(new_pos):
                perimeter += 1
            elif farm[new_pos] != color:
                perimeter += 1

    p1 += area * perimeter
    p2 += area * corner_count

print("p1", p1)
print("p2", p2)

io.imshow(label_img)
io.show()

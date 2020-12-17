import sys
import copy
from neighbors import neighbors_4d

lines = [line.strip() for line in sys.stdin]
space4 = [[[["." for x in range(len(lines[0])+12)] for y in range(len(lines)+12)] for z in range(13)] for w in range(13)]
for j, line in enumerate(lines):
    for i, c in enumerate(line):
        space4[6][6][j+6][i+6] = c

space_cpy = copy.deepcopy(space4)

def print_space(q):
    for w, space in enumerate(q):
        for z, plane in enumerate(space):
            print(f"z={z-6}, w={w-6}")
            print("\n".join(["".join(i) for i in plane]))
for cycle in range(6):
    for w, space in enumerate(space4):
        for z, plane in enumerate(space):
            for y, line in enumerate(plane):
                for x, cube in enumerate(line):
                    count = neighbors_4d(space4, w, z, y, x, "#")
                    if cube == "#":
                        if count in [2, 3]:
                            space_cpy[w][z][y][x] = "#"
                        else:
                            space_cpy[w][z][y][x] = "."
                    elif cube == ".":
                        if count == 3:
                            space_cpy[w][z][y][x] = "#"
                        else:
                            space_cpy[w][z][y][x] = "."
    space4 = copy.deepcopy(space_cpy)
print(str(space4).count('#'))

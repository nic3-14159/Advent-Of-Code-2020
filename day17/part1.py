import sys
import copy
from neighbors import neighbors_3d
lines = [line.strip() for line in sys.stdin]
space = [[["." for x in range(len(lines[0])+12)] for y in range(len(lines)+12)] for z in range(13)]
for j, line in enumerate(lines):
    for i, c in enumerate(line):
        space[6][j+6][i+6] = c

space_cpy = copy.deepcopy(space)

def print_space(q):
    for z, plane in enumerate(q):
        print(f"z={z-6}")
        print("\n".join(["".join(i) for i in plane]))

for cycle in range(6):
    for z, plane in enumerate(space):
        for y, line in enumerate(plane):
            for x, cube in enumerate(line):
                count = neighbors_3d(space, z, y, x, "#")
                if cube == "#":
                    if count in [2, 3]:
                        space_cpy[z][y][x] = "#"
                    else:
                        space_cpy[z][y][x] = "."
                elif cube == ".":
                    if count == 3:
                        space_cpy[z][y][x] = "#"
                    else:
                        space_cpy[z][y][x] = "."
        #if abs(z-6)<=cycle+1:
        #    print(f"z={z-6}")
        #    print("\n".join(["".join(i) for i in plane]))
    #print_space(space_cpy)
    #tmp = space_cpy
    #space = space_cpy
    #space_cpy = tmp
    #print_space(space)
    space = copy.deepcopy(space_cpy)
print(str(space).count('#'))

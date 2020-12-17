def neighbors_4d(space, w, z, y, x, char):
    count = 0
    for m in range(-1, 2):
        for k in range(-1, 2):
            for j in range(-1, 2):
                for i in range(-1, 2):
                    if w+m in range(len(space)) and z+k in range(len(space[0])) and y+j in range(len(space[0][0])) and x+i in range(len(space[0][0][0])):
                        if space[w+m][z+k][y+j][x+i] == char:
                            count += 1
    return count - (1 if space[w][z][y][x] == char else 0)


def neighbors_3d(space, z, y, x, char):
    count = 0
    for k in range(-1, 2):
        for j in range(-1, 2):
            for i in range(-1, 2):
                if z+k in range(len(space)) and y+j in range(len(space[0])) and x+i in range(len(space[0][0])):
                    if space[z+k][y+j][x+i] == char:
                        count += 1
    return count - (1 if space[z][y][x] == char else 0)

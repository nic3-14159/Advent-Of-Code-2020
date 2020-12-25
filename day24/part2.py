import sys
import copy
bestagons = set()
for line in sys.stdin:
    dir_buf = ""
    x = 0.0
    y = 0.0
    for c in line.strip():
        dir_buf += c
        if dir_buf in ["w", "e", "nw", "ne", "sw", "se"]:
            if dir_buf == "e":
                x += 1
            elif dir_buf == "w":
                x -= 1
            elif dir_buf == "nw":
                x -= 0.5
                y += 1
            elif dir_buf == "ne":
                x += 0.5
                y += 1
            elif dir_buf == "sw":
                x -= 0.5
                y -= 1
            elif dir_buf == "se":
                x += 0.5
                y -= 1
            dir_buf = ""
    if (x, y) in bestagons:
        bestagons.remove((x, y))
    else:
        bestagons.add((x, y))

neighbors = [(-0.5, 1), (0.5, 1), (-1, 0), (0, 0), (1, 0), (-0.5, -1), (0.5, -1)]
for _ in range(100):
    updated = copy.deepcopy(bestagons)
    for hexagon in bestagons:
        for n in [(hexagon[0] + a[0], hexagon[1] + a[1]) for a in neighbors]:
            count = 0
            for neighbor in neighbors:
                if (n[0] + neighbor[0], n[1] + neighbor[1]) in bestagons:
                    count += 1
            if n in bestagons:  # tile is black
                if count == 1 or count > 3:  # zero or >2 surrounding are black
                    updated.discard(n)  # set cell to white
            else:  # tile is white
                if count == 2:
                    updated.add(n)
    bestagons = copy.deepcopy(updated)
print(len(bestagons))

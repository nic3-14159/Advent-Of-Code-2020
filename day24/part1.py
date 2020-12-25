import sys
tiles = set()
count = 0
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
    if (x, y) in tiles:
        tiles.remove((x, y))
        count -= 1
    else:
        tiles.add((x, y))
        count += 1
print(count)

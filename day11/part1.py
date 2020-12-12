import sys
import copy

adj = [(-1,-1), (0,-1), (1, -1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]
if __name__ == "__main__":
    layout = [list(i.strip()) for i in list(sys.stdin)]
    changes = True
    while changes:
        print(*["".join(i) for i in layout], sep="\n")
        print()
        changes = False
        lines = copy.deepcopy(layout)
        for i, line in enumerate(layout):
            for j, c in enumerate(line):
                occ = 0
                for x, y in adj:
                    if 0 <= j+x < len(line) and 0 <= i+y < len(lines):
                        if layout[i+y][j+x] == "#":
                            occ += 1
                if c == "L" and occ == 0:
                    lines[i][j] = "#"
                    changes = True
                elif c == "#" and occ >= 4:
                    lines[i][j] = "L"
                    changes = True
        layout = copy.deepcopy(lines)
    count = 0
    for line in lines:
        for c in line:
            count += 1 if c == "#" else 0
    print(count)



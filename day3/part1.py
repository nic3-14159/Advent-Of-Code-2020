slope_map = list()
while True:
    try:
        slope_map.append(input())
    except EOFError:
        break

x = 0
y = 0
count = 0
while (y < len(slope_map)):
    count += (slope_map[y][x] == '#')
    x = (x+3) % len(slope_map[0])
    y += 1

print(count)

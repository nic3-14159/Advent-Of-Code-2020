slope_map = list()
while True:
    try:
        slope_map.append(input())
    except EOFError:
        break

count = [0 for i in range(5)]
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for i in range(5):
    x = 0
    y = 0
    while (y < len(slope_map)):
        count[i] += (slope_map[y][x] == '#')
        x = (x+slopes[i][0]) % len(slope_map[0])
        y += slopes[i][1]

product = count[0]
for i in range(1, 5):
    product *= count[i]
print(product)

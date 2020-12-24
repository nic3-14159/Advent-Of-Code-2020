cups = dict()
lables = [int(c) for c in input()]
lables = lables + list(range(max(lables)+1, 1000001))
curr_cup = lables[0]
dest_cup = curr_cup-1
for i, c in enumerate(lables):
    cups[c] = lables[(i+1) % len(lables)]

min_cup = min(cups)
for _ in range(10000000):
    picked_cups = list()
    tmp = curr_cup
    for i in range(3):
        picked_cups.append(cups[tmp])
        tmp = cups[tmp]
    cups[curr_cup] = cups[tmp]
    while dest_cup in picked_cups:
        dest_cup -= 1
        if dest_cup < min_cup:
            dest_cup = 1000000
    cups[picked_cups[2]] = cups[dest_cup]
    cups[dest_cup] = picked_cups[0]
    curr_cup = cups[curr_cup]
    dest_cup = curr_cup-1
    if dest_cup < min_cup:
        dest_cup = 1000000
print(cups[1] * cups[cups[1]])

cups = dict()
lables = input()
curr_cup = int(lables[0])
dest_cup = curr_cup-1
for i, c in enumerate(lables):
    cups[int(c)] = int(lables[(i+1) % len(lables)])

def print_cups():
    i = 1
    for _ in range(len(cups)-1):
        print(cups[i], end="")
        i = cups[i]
    print()

for _ in range(100):
    picked_cups = list()
    tmp = curr_cup
    for i in range(3):
        picked_cups.append(cups[tmp])
        tmp = cups[tmp]
    cups[curr_cup] = cups[tmp]
    while dest_cup in picked_cups:
        dest_cup -= 1
        if dest_cup < min(cups):
            dest_cup = max(cups)
    cups[picked_cups[2]] = cups[dest_cup]
    cups[dest_cup] = picked_cups[0]
    curr_cup = cups[curr_cup]
    dest_cup = curr_cup-1
    if dest_cup < min(cups):
        dest_cup = max(cups)
print_cups()

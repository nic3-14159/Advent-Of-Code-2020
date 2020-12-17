import sys
line = input()
fields = dict()
tickets = []
while line != "":
    field, ranges = line.split(":")
    fields[field.strip()] = [range(int(a), int(b)+1) for a, b in [i.strip().split("-") for i in ranges.split("or")]]
    line = input()
input()
your_ticket = [int(i) for i in input().split(",")]
input()
input()
while True:
    try:
        tickets.append([int(i) for i in input().split(",")])
    except EOFError:
        break


def check_values(valid_ranges, value):
    possible = set()
    for field in valid_ranges:
        for v_range in valid_ranges[field]:
            if value in v_range:
                possible.add(field)
    return possible

possible_fields = []
for ticket in tickets:
    field_map = list()
    for value in ticket:
        v = check_values(fields, value)
        if len(v) == 0:
            break
        field_map.append(v)
    else:
        possible_fields.append(field_map)

m = []
for i in range(0, 20):
    mapping = possible_fields[0][i]
    for f in possible_fields:
        mapping = mapping.intersection(f[i])
    m.append(mapping)

unique = 0
while unique < 20:
    unique = 0
    for i in range(0, 20):
        others = set()
        for j in range(0, 20):
            if j != i:
                others.update(m[j])
        if len(m[i].difference(others)) == 1:
            m[i] = m[i].difference(others)
            for j in range(0, 20):
                if j != i:
                    m[j].difference_update(m[i])
            unique += 1

output = 1
for i, field in enumerate([list(j)[0] for j in m]):
    if "departure" in field:
        print(field)
        output *= your_ticket[i]

print(output)

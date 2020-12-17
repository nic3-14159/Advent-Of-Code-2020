import sys
line = input()
fields = dict()
tickets = []
while line != "":
    field, ranges = line.split(":")
    fields[field.strip()] = [range(int(a), int(b)+1) for a, b in [i.strip().split("-") for i in ranges.split("or")]]
    line = input()
print(fields)
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
    for field in valid_ranges.values():
        for v_range in field:
            if value in v_range:
                return -1
    return value


error_rate = 0
for ticket in tickets:
    for value in ticket:
        v = check_values(fields, value)
        if v != -1:
            error_rate += v
print(error_rate)

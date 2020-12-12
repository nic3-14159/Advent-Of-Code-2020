import sys

if __name__ == "__main__":
    instructions = list(sys.stdin)
    x = 0
    y = 0
    waypoint = [10, 1]
    for i in instructions:
        direction = i[0]
        distance = int(i[1:])
        if direction == "N":
            waypoint[1] += distance
        elif direction == "S":
            waypoint[1] -= distance
        elif direction == "E":
            waypoint[0] += distance
        elif direction == "W":
            waypoint[0] -= distance
        elif direction == "L":
            for _ in range(distance//90):
                waypoint = [-waypoint[1], waypoint[0]]
        elif direction == "R":
            for _ in range(distance//90):
                waypoint = [waypoint[1], -waypoint[0]]
        elif direction == "F":
            x += waypoint[0]*distance
            y += waypoint[1]*distance
    print(abs(x)+abs(y))
        


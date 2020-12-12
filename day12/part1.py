import sys

if __name__ == "__main__":
    instructions = list(sys.stdin)
    x = 0
    y = 0
    facing = (1,0)
    for i in instructions:
        direction = i[0]
        distance = int(i[1:])
        if direction == "N":
            y += distance
        elif direction == "S":
            y -= distance
        elif direction == "E":
            x += distance
        elif direction == "W":
            x -= distance
        elif direction == "L":
            for i in range(distance//90):
                facing = (-facing[1], facing[0])
        elif direction == "R":
            for i in range(distance//90):
                facing = (facing[1], -facing[0])
        elif direction == "F":
            x += facing[0]*distance
            y += facing[1]*distance
        print(facing, x, y)
    print(abs(x)+abs(y))
        


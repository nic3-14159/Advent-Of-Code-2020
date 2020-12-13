import math

if __name__ == "__main__":
    input()
    ids = [int(i.replace("x", "-1")) for i in input().split(",")]
    t = ids[0]
    buses = [ids[0]]
    for i, bus_id in enumerate(ids):
        if i != 0 and bus_id != -1:
            while (t+i) % bus_id != 0:
                t += math.lcm(*buses)
            buses.append(bus_id)
    print(t)

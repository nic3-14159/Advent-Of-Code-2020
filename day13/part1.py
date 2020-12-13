import sys
import math

if __name__ == "__main__":
    estimate = int(input())
    ids = input().split(",")
    early = 100000000000
    early_bus = 0
    for i in ids:
        if i != "x":
            bus = int(i)
            if math.ceil(estimate/bus)*bus < early:
                early_bus = bus
                early = math.ceil(estimate/bus)*bus
    print((early-estimate)*early_bus)


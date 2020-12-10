import sys
dp = dict()
def count(prev, adapters):
    if (prev, sum(adapters)) in dp.keys():
        return dp[(prev, sum(adapters))]
    if len(adapters) == 1:
        return 1
    else:
        if adapters[1] - prev <= 3:
            dp[(prev, sum(adapters))] = count(prev, adapters[1:]) + count(adapters[0], adapters[1:])
            return dp[(prev, sum(adapters))]
        else:
            dp[(prev, sum(adapters))] = count(adapters[0], adapters[1:])
            return dp[(prev, sum(adapters))]


if __name__ == "__main__":
    a = sorted([int(i) for i in sys.stdin])
    print(count(0, a))

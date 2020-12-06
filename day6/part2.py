import sys

if __name__ == "__main__":
    groups = [i.split() for i in "".join(list(sys.stdin)).split("\n\n")]
    counts = 0
    for group in groups:
        g = [set(i) for i in group]
        for i in range(1, len(g)):
            g[0] = g[0].intersection(g[i])
        counts += len(g[0])
    print(counts)

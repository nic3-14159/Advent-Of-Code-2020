import sys

if __name__ == "__main__":
    groups = [set("".join(i.split())) for i in "".join(list(sys.stdin)).split("\n\n")]
    counts = 0
    for group in groups:
        counts += len(group)
    print(counts)

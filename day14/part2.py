import sys

if __name__ == "__main__":
    lines = [[i.strip() for i in line.split("=")] for line in sys.stdin]
    mem = dict()
    mask = ""
    for line in lines:
        if line[0] == "mask":
            mask = line[1]
        else:
            value = int(line[1])
            for i in range(2**mask.count("X")):
                floating = [int(c) for c in "{num:0{size}b}".format(num=i, size=mask.count("X"))]
                addr = int(line[0][4:-1])
                for j, bit in enumerate(mask):
                    if bit == "X":
                        b = floating.pop(0) << 35-j
                        addr = addr & ~(1 << 35-j) | b
                    else:
                        addr |= int(bit) << 35-j
                mem[addr] = value
    print(sum(mem.values()))

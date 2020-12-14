import sys

if __name__ == "__main__":
    lines = [[i.strip() for i in line.split("=")] for line in sys.stdin]
    print(lines)
    mem = dict()
    mask = ""
    for line in lines:
        if line[0] == "mask":
            mask = line[1]
        else:
            binary = "{:036b}".format(int(line[1]))
            addr = int(line[0][4:-1])
            result = [binary[i] if bit == "X" else bit for i, bit in enumerate(mask)]
            value = int("".join(result), base=2)
            mem[addr] = value
    print(sum(mem.values()))

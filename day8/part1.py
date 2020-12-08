import sys

if __name__ == "__main__":
    f = open("input", "r")
    instructions = [line.split() for line in f]
    visited = [False for _ in instructions]
    print(instructions)
    acc = 0
    pointer = 0
    while not visited[pointer]:
        inst = instructions[pointer][0]
        value = int(instructions[pointer][1])
        print(pointer, inst, value)
        visited[pointer] = True
        if inst == "acc":
            acc += value
            pointer += 1
        elif inst == "jmp":
            pointer += value
        elif inst == "nop":
            pointer += 1
    print(acc)
    f.close()

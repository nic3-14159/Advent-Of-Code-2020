import sys

def execute(instructions):
    acc = 0
    pointer = 0
    visited = [False for _ in instructions]
    while pointer != len(instructions) and not visited[pointer]:
        inst = instructions[pointer][0]
        value = int(instructions[pointer][1])
        visited[pointer] = True
        if inst == "acc":
            acc += value
            pointer += 1
        elif inst == "jmp":
            pointer += value
        elif inst == "nop":
            pointer += 1
    return (pointer, acc)

if __name__ == "__main__":
    instructions = [line.split() for line in sys.stdin]
    for i, [inst, value] in enumerate(instructions):
        if inst == "nop":
            instructions[i][0] = "jmp"
            pointer, acc = execute(instructions)
            if pointer == len(instructions):
                print(acc)
                break
            else:
                instructions[i][0] = "nop"
        elif inst == "jmp":
            instructions[i][0] = "nop"
            pointer, acc = execute(instructions)
            if pointer == len(instructions):
                print(acc)
                break
            else:
                instructions[i][0] = "jmp"

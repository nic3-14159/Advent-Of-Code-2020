import sys
count = 0


def eval_math(expr):
    acc = list()
    op_stack = list()
    b = None
    ld_acc = [True]
    for c in expr:
        if ld_acc[-1] and c.isdigit():
            acc.append(int(c))
            ld_acc[-1] = False
        elif not c.isspace():
            if c in ["+", "*"]:
                op_stack.append(c)
            elif c == "(":
                ld_acc.append(True)
            elif c == ")":
                ld_acc.pop()
                if not ld_acc[-1]:
                    b = acc.pop()
                else:
                    ld_acc[-1] = False
            elif c.isdigit():
                b = int(c)
            if b is not None:
                op = op_stack.pop()
                if op == "*":
                    acc[-1] *= b
                    b = None
                elif op == "+":
                    acc[-1] += b
                    b = None
    return acc[0]

for line in sys.stdin:
    expr = line.strip()
    count += eval_math(expr)
print(count)

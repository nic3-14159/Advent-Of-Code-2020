import sys
count = 0


# Learned about shunting yard algorithm
# Useful links:
# http://www.wcipeg.com/wiki/Shunting_yard_algorithm
# https://brilliant.org/wiki/shunting-yard-algorithm

def eval_math(expr):
    out_stack = list()
    op_stack = list()
    expr = f"({expr})"
    b = None
    for c in expr:
        if c.isdigit():
            out_stack.append(int(c))
        elif c in ["+", "*", "(", ")"]:
            if c == "+":
                op_stack.append(c)
            elif c == "*":
                while op_stack[-1] == "+":
                    b = out_stack.pop(-1)
                    out_stack[-1] = out_stack[-1] + b
                    op_stack.pop()
                op_stack.append(c)
            elif c == "(":
                op_stack.append(c)
            elif c == ")":
                while op_stack[-1] != "(":
                    b = out_stack.pop()
                    if op_stack[-1] == "+":
                        out_stack[-1] = out_stack[-1] + b
                    else:
                        out_stack[-1] = out_stack[-1] * b
                    op_stack.pop()
                op_stack.pop()
    return out_stack[0]


for line in sys.stdin:
    expr = line.strip()
    print(eval_math(expr))
    count += eval_math(expr)
print(count)

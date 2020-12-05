import sys

if __name__ == "__main__":
    p = list(sys.stdin)
    high_id = 0
    for b_pass in p:
        r_low = 0
        r_high = 127
        s_low = 0
        s_high = 7
        for c in b_pass:
            if c == 'F':
                r_high = (r_low + r_high)//2
            elif c == 'B':
                low = (r_low + r_high)//2
            elif c == 'R':
                s_low = (s_low + s_high)//2
            elif c == 'L':
                s_high = (s_low + s_high)//2
        high_id = max(high_id, r_high*8 + s_high)
    print(high_id)

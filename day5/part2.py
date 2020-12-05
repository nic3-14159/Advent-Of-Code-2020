import sys

if __name__ == "__main__":
    p = list(sys.stdin)
    high_id = 0
    seats = list()
    for b_pass in p:
        low = 0
        high = 127
        s_low = 0
        s_high = 7
        for c in b_pass:
            if c == 'F':
                high = (low+high)//2
            elif c == 'B':
                low = (low+high)//2
            elif c == 'R':
                s_low = (s_low+s_high)//2
            elif c == 'L':
                s_high = (s_low+s_high)//2
        seats.append(high*8 + s_high)
    seats.sort()
    for i in range(1, len(seats)):
        if seats[i] == seats[i-1]+2:
            print(seats[i]-1)
            break

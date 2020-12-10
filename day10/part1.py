import sys

if __name__ == "__main__":
    a = sorted([int(i) for i in sys.stdin])
    a.insert(0,0)
    builtin = max(a)+3
    a.append(builtin)
    num1 = 0
    num3 = 0
    for i in range(1, len(a)):
        print(a[i] - a[i-1])
        if a[i] - a[i-1] == 1:
            num1+=1 
        if a[i] - a[i-1] ==3:
            num3+=1
    print(num1 * num3)

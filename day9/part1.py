import sys

if __name__ == "__main__":
    nums = [int(line) for line in sys.stdin]
    pre = []
    for n in nums:
        if len(pre) == 25:
            for i, j in enumerate(pre):
                if n-j in pre[i:]:
                    break
            else:
                print(n)
                break
            pre.pop(0)
        pre.append(n)

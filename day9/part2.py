import sys

if __name__ == "__main__":
    target = 0
    nums = [int(line) for line in sys.stdin]
    pre = []
    for n in nums:
        if len(pre) == 25:
            for i, j in enumerate(pre):
                if n-j in pre[i:]:
                    break
            else:
                target = n
                break
            pre.pop(0)
        pre.append(n)

    for length in range(2, len(nums)):
        for i in range(0, len(nums)-length+1):
            if sum(nums[i:i+length]) == target:
                print(min(nums[i:i+length])+max(nums[i:i+length]))
                sys.exit()

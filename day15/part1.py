if __name__ == "__main__":
    spoken = dict()
    nums = [int(i) for i in input().split(",")]
    last = 0
    for turn in range(2020):
        if turn < len(nums):
            spoken[nums[turn]] = list()
            spoken[nums[turn]].append(turn)
            last = nums[turn]
        else:
            if len(spoken[last]) == 1:
                if 0 not in spoken.keys():
                    spoken[0] = list()
                spoken[0].append(turn)
                last = 0
            else:
                age = spoken[last][-1] - spoken[last][-2]
                if age not in spoken.keys():
                    spoken[age] = list()
                spoken[age].append(turn)
                last = age
    print(last)

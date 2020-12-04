count = 0
keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
while True:
    line = input().split()
    passport = dict()
    try:
        while len(line) != 0:
            for field in line:
                tmp = field.split(":")
                passport[tmp[0]] = tmp[1]
            line = input().split()
        print(passport)
        for key in keys:
            if key not in passport.keys():
                break
        else:
            count += 1
        print(count)
            
    except EOFError:
        for key in keys:
            if key not in passport.keys():
                break
        else:
            count += 1
        break

print(count)

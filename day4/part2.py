count = 0
keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def is_valid(passport):
    for key in keys:
        if key not in passport.keys():
            return False

        if key == "byr" and not (1920 <= int(passport[key]) <= 2002):
            return False

        if key == "iyr" and not (2010 <= int(passport[key]) <= 2020):
            return False

        if key == "eyr" and not (2020 <= int(passport[key]) <= 2030):
            return False

        if key == "hgt":
            if passport[key][-2:] == "in":
                if not (59 <= int(passport[key][0:-2]) <= 76):
                    return False
            elif passport[key][-2:] == "cm":
                if not (150 <= int(passport[key][0:-2]) <= 193):
                    return False
            else:
                return False

        if key == "hcl":
            if len(passport[key]) == 7 and passport[key][0] == "#":
                for c in passport[key][1:]:
                    if not ('a' <= c <= 'f') and not c.isdigit():
                        return False
            else:
                return False

        if key == "ecl" and passport[key] not in ["amb", "blu", "brn", "gry", "grn",  "hzl", "oth"]:
            return False

        if key == "pid":
            if len(passport[key]) != 9 or not passport[key].isdigit():
                return False

    return True


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
        count += 1 if is_valid(passport) else 0
        print(count)
            
    except EOFError:
        count += 1 if is_valid(passport) else 0
        break

print(count)

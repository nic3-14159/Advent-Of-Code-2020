import sys


def is_valid(passport):
    keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for key in keys:
        if key not in passport.keys():
            return False

        elif key == "byr" and not (1920 <= int(passport[key]) <= 2002):
            return False

        elif key == "iyr" and not (2010 <= int(passport[key]) <= 2020):
            return False

        elif key == "eyr" and not (2020 <= int(passport[key]) <= 2030):
            return False

        elif key == "hgt":
            if passport[key][-2:] == "in":
                if not (59 <= int(passport[key][0:-2]) <= 76):
                    return False
            elif passport[key][-2:] == "cm":
                if not (150 <= int(passport[key][0:-2]) <= 193):
                    return False
            else:
                return False

        elif key == "hcl":
            if len(passport[key]) == 7 and passport[key][0] == "#":
                for c in passport[key][1:]:
                    if not ('a' <= c <= 'f') and not c.isdigit():
                        return False
            else:
                return False

        elif key == "ecl" and passport[key] not in ["amb", "blu", "brn", "gry", "grn",  "hzl", "oth"]:
            return False

        elif key == "pid":
            if len(passport[key]) != 9 or not passport[key].isdigit():
                return False

    return True


if __name__ == "__main__":
    sections = [i.split() for i in "".join(list(sys.stdin)).split("\n\n")]
    passports = [dict([i.split(":") for i in p]) for p in sections]
    valid = [is_valid(p) for p in passports]
    print(sum(valid))

import sys


def is_valid(passport):
    keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for key in keys:
        if key not in passport.keys():
            return False
    return True


if __name__ == "__main__":
    sections = [i.split() for i in "".join(list(sys.stdin)).split("\n\n")]
    passports = [dict([i.split(":") for i in p]) for p in sections]
    valid = [is_valid(p) for p in passports]
    print(sum(valid))

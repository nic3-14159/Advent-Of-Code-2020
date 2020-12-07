import sys


def count_bags(rules, outer_bag):
    if outer_bag == "no other":
        return 1
    count = 0
    for bag in rules[outer_bag].keys():
        count += rules[outer_bag][bag]*count_bags(rules, bag)
        count += rules[outer_bag][bag]
    return count


def preprocess(rule, keep_digits=False):
    rule = rule.replace("bags", "")
    rule = rule.replace("bag", "")
    rule = rule.replace(".", "")
    rule = rule.strip()
    output = ""
    if not keep_digits:
        for c in rule:
            if not c.isdigit():
                output += c
        return output
    return rule


def get_count(rule):
    rule = preprocess(rule, keep_digits=True)
    count = "0"
    value = ""
    for c in rule:
        if c.isdigit():
            count += c
        else:
            value += c
    return (value.strip(), int(count))


if __name__ == "__main__":
    rules = {preprocess(k): v for k, v in [[i.strip() for i in line.strip().split("contain")] for line in sys.stdin]}
    for bag in rules.keys():
        rules[bag] = {k: v for k, v in [get_count(i) for i in rules[bag].split(",")]}
    print(count_bags(rules, "shiny gold"))

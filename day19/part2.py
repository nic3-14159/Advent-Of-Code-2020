import sys
import regex


def make_regex(rule_dict, num):
    output = "("
    if num == 8:
        return f"({make_regex(rule_dict, 42)}+)"
    if num == 11:
        return f"(?<r>{make_regex(rule_dict, 42)}(?&r)?{make_regex(rule_dict, 31)})"
    for tok in rule_dict[num].split():
        if tok.isdigit():
            output += make_regex(rule_dict, int(tok))
        else:
            output += tok.replace('"', '')
    return output+")"


rules = dict()
messages = list()
read_rules = True
for line in sys.stdin:
    if line.strip() == "":
        read_rules = False
    elif read_rules:
        rule, pattern = line.split(":")
        rules[int(rule.strip())] = pattern.strip()
    else:
        messages.append(line.strip())

rule_0 = regex.compile(make_regex(rules, 0)+"$")
count = 0
for line in messages:
    count += 1 if regex.match(rule_0, line) else 0

print(count)

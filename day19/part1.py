import sys
import re


def make_regex(rule_dict, num):
    output = "("
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

rule_0 = re.compile(make_regex(rules, 0) + "$")
count = 0
for line in messages:
    count += 1 if re.match(rule_0, line) else 0
print(count)

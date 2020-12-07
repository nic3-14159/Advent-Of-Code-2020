import sys
def shiny_gold(rules, bag):
    if "shiny gold" in rules[bag]:
        return True
    elif "no other" in rules[bag]:
        return False
    else:
        for bag in rules[bag]:
            if shiny_gold(rules, bag):
                return True
        else:
            return False

def preprocess(rule):
    rule = rule.replace("bags","")
    rule = rule.replace("bag","")
    rule = rule.replace(".", "")
    rule = rule.strip()
    output = ""
    for c in rule:
        if not c.isdigit():
            output += c
    return output

if __name__ == "__main__":
    rules = {preprocess(k):v for k,v in [[i.strip() for i in line.strip().split("contain")] for line in sys.stdin]}
    for bag in rules.keys():
        rules[bag] = [preprocess(i).strip() for i in rules[bag].split(",")]
    print(rules)
    count = 0
    for bag in rules.keys():
        count += shiny_gold(rules, bag)
    print(count)
     

import sys
ingredients = list()
allergen_counts = dict()
allergen_tbl = dict()
pos_allergens = set()
ingredient_counts = dict()
counts = dict()
for line in sys.stdin:
    ingredient, allergen_raw = line.split("(contains")
    ingredients.append(ingredient.split())
    allergens = allergen_raw.strip()[:-1].split(", ")
    for n, i in enumerate(ingredient.split()):
        if i not in ingredient_counts:
            ingredient_counts[i] = 0
        ingredient_counts[i] += 1
        for a in allergens:
            if a not in allergen_counts:
                allergen_counts[a] = 0
            if a not in counts:
                counts[a] = dict()
            if i not in counts[a]:
                counts[a][i] = 0
            counts[a][i] += 1
            allergen_counts[a] += 1 if n == 0 else 0


while len(allergen_tbl) < len(counts):
    for a in allergen_counts:
        found_allergen = ""
        for i in counts[a]:
            if counts[a][i] >= allergen_counts[a]:
                if found_allergen == "":
                    found_allergen = i
                else:
                    found_allergen = ""
                    break
        if found_allergen != "":
            allergen_tbl[a] = found_allergen
    for a, ingredient in allergen_tbl.items():
        for allergen in counts:
            counts[allergen].pop(ingredient, None)

print(*[i[1] for i in sorted(allergen_tbl.items())], sep=",")

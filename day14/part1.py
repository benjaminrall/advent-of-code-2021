with open("input.txt", "r") as f:
    lines = [line.replace("\n", "") for line in f.readlines()]

polymer = [lines[0][i] + lines[0][i + 1] for i in range(len(lines[0]) - 1)]

lines = [rule.split(" -> ") for rule in lines[2:]]
rules = {rule[0]:rule[1] for rule in lines}

steps = 10
for step in range(steps):
    newPolymer = []
    for pair in polymer:
        newPolymer.append(pair[0] + rules[pair])
        newPolymer.append(rules[pair] + pair[1])
    polymer = newPolymer
polymerString = ''.join([polymer[0][0]] + [pair[1] for pair in polymer])

characters = []
for char in polymerString:
    if char not in characters:
        characters.append(char)
counts = []
for char in characters:
    counts.append(polymerString.count(char))
print(max(counts) - min(counts))
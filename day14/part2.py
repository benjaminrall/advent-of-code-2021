with open("input.txt", "r") as f:
    lines = [line.replace("\n", "") for line in f.readlines()]

polymerString = lines[0]
polymer = {}
for i in range(len(polymerString) - 1):
    pair = polymerString[i] + polymerString[i + 1]
    polymer[pair] = polymer[pair] + 1 if pair in polymer else 1

lines = [rule.split(" -> ") for rule in lines[2:]]
rules = {rule[0]:rule[1] for rule in lines}

steps = 40
for step in range(steps):
    newPolymer = {}
    for pair in polymer:
        newPairs = (pair[0] + rules[pair], rules[pair] + pair[1])
        for newPair in newPairs:
            newPolymer[newPair] = newPolymer[newPair] + polymer[pair] if newPair in newPolymer else polymer[pair]
    polymer = newPolymer

characterCounts = {}
for pair in polymer:
    for char in pair:
        characterCounts[char] = characterCounts[char] + polymer[pair] if char in characterCounts else polymer[pair]
for char in characterCounts:
    characterCounts[char] //= 2
characterCounts[polymerString[0]] += 1
characterCounts[polymerString[-1]] += 1
minmax = [None, None]
for char in characterCounts:
    if minmax[0] is None or characterCounts[char] < minmax[0]:
        minmax[0] = characterCounts[char]
    if minmax[1] is None or characterCounts[char] > minmax[1]:
        minmax[1] = characterCounts[char]
print(minmax[1] - minmax[0])
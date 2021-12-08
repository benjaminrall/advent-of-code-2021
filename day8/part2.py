with open("input.txt", "r") as f:
    lines = [line.replace("\n", "").split(" | ") for line in f.readlines()]

data = [ [line[0].split(" "), line[1].split(" ")] for line in lines ]

digits = {0:[0,1,2,4,5,6], 1:[2,5], 2:[0,2,3,4,6], 3:[0,2,3,5,6], 4:[1,2,3,5],
          5:[0,1,3,5,6], 6:[0,1,3,4,5,6], 7:[0,2,5], 8:[0,1,2,3,4,5,6], 9:[0,1,2,3,5,6]}

alphabet = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g'}

s = 0
for line in data:
    canBe = {alphabet[i]:[j for j in range(7)] for i in range(7)}
    cantBe = {alphabet[i]:[] for i in range(7)}
    wiring = {alphabet[i]:-1 for i in range(7)}
    found = []
    inputLines = line[0]
    output = line[1]
    # Initial deductions
    for digit in inputLines:
        if len(digit) == 2:
            for key in cantBe:
                if key not in digit:
                    cantBe[key] += digits[1]
        if len(digit) == 4:
            for key in cantBe:
                if key not in digit:
                    cantBe[key] += digits[4]
        if len(digit) == 3:
            for key in cantBe:
                if key not in digit:
                    cantBe[key] += digits[7]
        if len(digit) == 7:
            for key in cantBe:
                if key not in digit:
                    cantBe[key] += digits[8]
    for key in canBe:
        cantBe[key] = list(dict.fromkeys(cantBe[key]))
        canBe[key] = list(dict.fromkeys([ x for x in canBe[key] if x not in cantBe[key]]))
    oldCanBe = []
    # Number deductions
    while -1 in [wiring[key] for key in wiring] and oldCanBe != canBe:
        oldCanBe = canBe.copy()
        toDeduce = []
        found = []
        for i, key in enumerate(canBe):
            if len(canBe[key]) == 1:
                toDeduce.append(canBe[key].copy())
                wiring[key] = canBe[key][0]
            if len(canBe[key]) == 2 and found.count(canBe[key]) == 1:
                toDeduce.append(canBe[key].copy())
            found.append(canBe[key])
        for deduction in toDeduce:
            if len(deduction) == 1:
                for key in canBe:
                    if deduction[0] in canBe[key]:
                        canBe[key].remove(deduction[0]) 
            if len(deduction) == 2:
                for key in canBe:
                    if canBe[key] != deduction:
                        canBe[key] = [x for x in canBe[key] if x not in deduction]
    # Final deduction
    if -1 in [wiring[key] for key in wiring]:
        pairsToSolve = []
        for key in canBe:
            if canBe[key] not in pairsToSolve and len(canBe[key]) == 2:
                pairsToSolve.append(canBe[key])
        p = len(pairsToSolve)
        mappings = []
        for i in range(2 ** p):
            mapping = wiring.copy()
            found = []
            for key in canBe:
                if canBe[key] in pairsToSolve:
                    n = pairsToSolve.index(canBe[key])
                    k = (i % (2 ** (n + 1))) // (2 ** n)
                    if canBe[key] not in found:
                        mapping[key] = canBe[key][k]
                        found.append(canBe[key])
                    else:
                        mapping[key] = canBe[key][(k + 1) % 2]
            mappings.append(mapping)
        validMapping = None
        for mapping in mappings:
            valid = True
            numberCombos = [sorted([mapping[c] for c in digit]) for digit in inputLines + output]
            for combo in numberCombos:
                if combo not in [digits[key] for key in digits]:
                    valid = False
                    break
            if valid:
                validMapping = mapping.copy()
        wiring = validMapping
        outputNums = [sorted([wiring[c] for c in digit]) for digit in output]
        outputDigit = ""
        for num in outputNums:
            for key in digits:
                if digits[key] == num:
                    outputDigit += str(key)
        s += int(outputDigit)
print(s)
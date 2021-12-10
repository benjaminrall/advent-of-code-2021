from collections import deque

with open("input.txt", "r") as f:
    chunks = [line.replace("\n", "") for line in f.readlines()]

closing = {'(':')', '[':']', '{':'}', '<':'>'}

def find_corrupted_chunk(chunk, i, opening):
    if opening not in closing:
        return (False, opening), i
    i += 1
    while i < len(chunk) - 1 and chunk[i] in closing:
        returnExpression, i = find_corrupted_chunk(chunk, i, chunk[i])
        if not returnExpression[0]:
            return returnExpression, i
        i += 1
    if i >= len(chunk):
        return (True, None), i
    if chunk[i] == closing[opening]:
        return (True, None), i
    if i < len(chunk):
        return (False, chunk[i]), i
    return (True, None), i

scoring = {')':1, ']':2, '}':3, '>':4}

totalScores = []
for chunk in chunks:
    results = find_corrupted_chunk(chunk, 0, chunk[0])[0]
    if not (not results[0] and results[1] not in closing):
        stack = deque()
        for char in chunk:
            if char in closing:
                stack.append(char)
            else:
                stack.pop()
        ending = ""
        while len(stack) > 0:
            ending += closing[stack.pop()]
        score = 0
        for char in ending:
            score *= 5
            score += scoring[char]
        totalScores.append(score)
print(sorted(totalScores)[(len(totalScores) - 1) // 2])
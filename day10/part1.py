with open("input.txt", "r") as f:
    chunks = [line.replace("\n", "") for line in f.readlines()]

scoring = {')':3, ']':57, '}':1197, '>':25137}
closing = {'(':')', '[':']', '{':'}', '<':'>'}

def start_chunk(chunk, i, opening):
    if opening not in closing:
        return (False, opening), i
    i += 1
    while i < len(chunk) - 1 and chunk[i] in closing:
        returnExpression, i = start_chunk(chunk, i, chunk[i])
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
    
score = 0
for chunk in chunks:
    results = start_chunk(chunk, 0, chunk[0])[0]
    print(results)
    if not results[0] and results[1] not in closing:
        score += scoring[results[1]]
print(score)
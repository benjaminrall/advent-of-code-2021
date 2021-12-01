with open("input.txt", "r") as f:
    lines = [int(line.replace("\n", "")) for line in f.readlines()]

currentLine = lines[0]
increments = 0
for line in lines[1:]:
    if line > currentLine:
        increments += 1
    currentLine = line

print(increments)

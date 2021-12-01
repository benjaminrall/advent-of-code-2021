with open("input.txt", "r") as f:
    lines = [int(line.replace("\n", "")) for line in f.readlines()]

sums = []
for i in range(len(lines) - 2):
    sums.append(sum(lines[i:i+3]))

currentLine = sums[0]
increments = 0
for line in sums[1:]:
    if line > currentLine:
        increments += 1
    currentLine = line

print(increments)
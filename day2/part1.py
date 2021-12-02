with open("input.txt","r") as f:
    lines = [line.replace("\n", "").split(" ") for line in f.readlines()]
lines = [(line[0], int(line[1])) for line in lines]

horizontal = 0
depth = 0

for line in lines:
    if line[0] == "forward":
        horizontal += line[1]
    elif line[0] == "up":
        depth -= line[1]
    elif line[0] == "down":
        depth += line[1]

print(horizontal * depth)
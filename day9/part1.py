with open("input.txt", "r") as f:
    lines = [[int(digit) for digit in line.replace("\n", "")] for line in f.readlines()]

def find_adjacent(x, y, basin, lines):
    basin.append((x, y))
    # top
    if y > 0 and lines[y - 1][x] < 9 and ((x, y - 1) not in basin):
        basin = find_adjacent(x, y - 1, basin, lines)
    # right
    if x < len(lines[0]) - 1 and lines[y][x + 1] < 9 and ((x + 1, y) not in basin):
        basin = find_adjacent(x + 1, y, basin, lines)
    # left
    if x > 0 and lines[y][x - 1] < 9 and ((x - 1, y) not in basin):
        basin = find_adjacent(x - 1, y, basin, lines)
    # bottom
    if y < len(lines) - 1 and lines[y + 1][x] < 9 and ((x, y + 1) not in basin):
        basin = find_adjacent(x, y + 1, basin, lines)
    return basin

dimensions = (len(lines[0]), len(lines))
basinSizes = []
for y in range(dimensions[1]):
    for x in range(dimensions[0]):
        data = lines[y][x]
        condition1 = y == 0 or data < lines[y - 1][x]
        condition2 = x == 0 or data < lines[y][x - 1]
        condition3 = y == dimensions[1] - 1 or data < lines[y + 1][x]
        condition4 = x == dimensions[0] - 1 or data < lines[y][x + 1]

        if condition1 and condition2 and condition3 and condition4:
            basin = find_adjacent(x, y, [], lines)
            basinSizes.append(len(basin))

n = sorted(basinSizes, reverse=True)[0:3]
print(n[0] * n[1] * n[2])
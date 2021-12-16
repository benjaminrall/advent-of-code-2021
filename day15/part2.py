import math

def find_min(indexes, distances):
    minDist = (math.inf, None)
    for index in indexes:
        if distances[index[0]][index[1]] < minDist[0]:
            minDist = (distances[index[0]][index[1]], index)
    return minDist

with open("input.txt", "r") as f:
    grid = [[int(risk) for risk in line.replace("\n", "")] for line in f.readlines()]

sRows = len(grid)
sCols = len(grid[0])
rows = sRows * 5
cols = sCols * 5
biggerGrid = [[None for col in range(cols)] for row in range(rows)]
for row in range(rows):
    for col in range(cols):
        addition = (row // sRows) + (col // sCols)
        newNum = grid[row % sRows][col % sCols] + addition
        newNum = newNum if newNum < 10 else newNum - 9
        biggerGrid[row][col] = newNum
grid = biggerGrid

distances = [[math.inf for _ in row] for row in grid]
previous = [[None for _ in row] for row in grid]
distances[0][0] = 0
toExamine = [(row, col) for row in range(rows) for col in range(cols)]
while len(toExamine) > 0:
    ud, ui = find_min(toExamine, distances)
    toExamine.remove(ui)
    if ui == (rows - 1, cols - 1):
        break
    for vi in [index for index in toExamine if (abs(index[0] - ui[0]) == 1 and index[1] - ui[1] == 0) or (abs(index[1] - ui[1]) == 1 and index[0] - ui[0] == 0)]:
        alt = ud + grid[vi[0]][vi[1]]
        if alt < distances[vi[0]][vi[1]]:
            distances[vi[0]][vi[1]] = alt
            previous[vi[0]][vi[1]] = ui
print(ud)
with open("input.txt", "r") as f:
    lines = [line.replace("\n", "") for line in f.readlines()]

points = []
folds = []
firstSection = True
for line in lines:
    if line == "":
        firstSection = False
        continue
    if firstSection:
        coord = line.split(",")
        points.append((int(coord[0]), int(coord[1])))
    else:
        fold = line.split(" ")[-1]
        folds.append((int(fold[2:]), fold[:1]))

foldsToMake = len(folds)
for i in range(foldsToMake):
    fold = folds[i]
    toRemove = []
    if fold[1] == 'x':
        for point in points:
            if point[0] > fold[0]:
                toRemove.append(point)
                newPoint = (fold[0] - (point[0] - fold[0]), point[1])
                if newPoint not in points:
                    points.append(newPoint)
    else:
        for point in points:
            if point[1] > fold[0]:
                toRemove.append(point)
                newPoint = (point[0], fold[0] - (point[1] - fold[0]))
                if newPoint not in points:
                    points.append(newPoint)
    for point in toRemove:
        points.remove(point)

max = [0, 0]
for point in points:
    if point[0] > max[0]:
        max[0] = point[0]
    if point[1] > max[1]:
        max[1] = point[1]

grid = [['.' for x in range(max[0] + 1)] for y in range(max[1] + 1)]
for point in points:
    grid[point[1]][point[0]] = '#'
for line in grid:
    print(line)
with open("input.txt", "r") as f:
    area = f.readline().replace("\n", "")
xBounds = [int(x) for x in area[area.index('x=') + 2:area.index(',')].split('..')]
yBounds = [int(y) for y in area[area.index('y=') + 2:].split('..')]

maxY = 0
for x in range(100):
    for y in range(1000):
        velocity = [x, y]
        position = [0, 0]
        midMaxY = 0
        while position[0] <= xBounds[1] and position[1] >= yBounds[0]:
            position = [position[i] + velocity[i] for i in range(2)]
            velocity[0] = 0 if velocity[0] == 0 else (velocity[0] - 1 if velocity[0] > 0 else velocity[0] + 1)
            velocity[1] -= 1
            if position[1] > midMaxY:
                midMaxY = position[1]
            if position[0] >= xBounds[0] and position[0] <= xBounds[1] and position[1] >= yBounds[0] and position[1] <= yBounds[1]:
                if midMaxY > maxY:
                    maxY = midMaxY
                break

print(maxY)
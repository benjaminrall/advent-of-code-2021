with open("input.txt", "r") as f:
    lines = [line.replace("\n", "") for line in f.readlines()]

octopi = [[int(c) for c in line] for line in lines]
count = len(octopi) * len(octopi[0])

steps = 500
flashes = 0
for i in range(steps):
    flashing = []
    flashes = 0
    for y in range(len(octopi)):
        for x in range(len(octopi[0])):
            octopi[y][x] += 1
            if octopi[y][x] > 9:
                flashing.append((x, y))
                octopi[y][x] = 0
    for coord in flashing:
        flashes += 1
        x = coord[0]
        y = coord[1]
        for ax in [-1, 0, 1]:
            for ay in [-1, 0, 1]:
                nx = x + ax
                ny = y + ay
                if nx >= 0 and nx < len(octopi[0]) and ny >= 0 and ny < len(octopi):
                    if octopi[ny][nx] != 0:
                        octopi[ny][nx] += 1
                    if octopi[ny][nx] > 9:
                        flashing.append((nx, ny))
                        octopi[ny][nx] = 0
    if flashes == count:
        print(i + 1)
        break
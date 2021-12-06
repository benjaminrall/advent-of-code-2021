import math

with open("input.txt", "r") as f:
    lines = [line.replace("\n", "") for line in f.readlines()]
vents = [ line.split(" -> ") for line in lines]
vents = [ [[int(e) for e in vent[0].split(",")], [int(e) for e in vent[1].split(",")]] for vent in vents ]

vent_area = {}
for vent in vents:
    if not (vent[0][0] == vent[1][0] or vent[0][1] == vent[1][1]):
        continue
    if vent[0][0] == vent[1][0]:
        diff = vent[1][1] - vent[0][1]
        for i in range(abs(diff) + 1):
            key = (vent[0][0], (vent[0][1] + i if diff > 0 else vent[0][1] - i))
            if key not in vent_area:
                vent_area[key] = 1
            else:
                vent_area[key] += 1
    elif vent[0][1] == vent[1][1]:
        diff = vent[1][0] - vent[0][0]
        for i in range(abs(diff) + 1):
            key = ((vent[0][0] + i if diff > 0 else vent[0][0] - i), vent[1][1])
            if key not in vent_area:
                vent_area[key] = 1
            else:
                vent_area[key] += 1
result = 0
for key in vent_area:
    if vent_area[key] >= 2:
        result += 1
print(result)
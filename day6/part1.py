with open("input.txt", "r") as f:
    lanternFish = [ int(e) for e in f.readline().split(",") ]

days = 80
for day in range(days):
    toAdd = 0
    for i in range(len(lanternFish)):
        if lanternFish[i] > 0:
            lanternFish[i] -= 1
        else:
            lanternFish[i] = 6
            toAdd += 1
    for i in range(toAdd):
        lanternFish.append(8)
    print(f"Day {day + 1} finished.")

print(len(lanternFish))
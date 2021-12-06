with open("input.txt", "r") as f:
    line = [ int(e) for e in f.readline().split(",") ]

lanternFish = {i - 1:0 for i in range(10)}
for e in line:
    lanternFish[e] += 1

days = 1000000
for day in range(days):
    for key in lanternFish:
        if key >= 0:
            lanternFish[key - 1] = lanternFish[key]
            lanternFish[key] = 0
    lanternFish[6] += lanternFish[-1]
    lanternFish[8] += lanternFish[-1]
    lanternFish[-1] = 0

count = 0
for key in lanternFish:
    count += lanternFish[key]
print(count)
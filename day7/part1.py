with open("input.txt","r") as f:
    line = [int(e) for e in f.readline().split(",")]

result = [sum([sum([ x + 1 for x in range(abs(e - i))]) for e in line]) for i in line]

print(min(result))
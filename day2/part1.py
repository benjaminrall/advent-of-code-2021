print(sum([line[1] for line in [(line[0], int(line[1])) for line in [line.replace("\n", "").split(" ") for line in open("input.txt","r").readlines()]] if line[0] == "forward"]) * sum(line[1] if line[0] == "down" else -line[1] for line in [(line[0], int(line[1])) for line in [line.replace("\n", "").split(" ") for line in open("input.txt","r").readlines()]] if line[0] == "up" or line[0] == "down"))
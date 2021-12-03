with open("input.txt", "r") as f:
    lines = [line.replace("\n", "") for line in f.readlines()]

oxygenRating = [[int(char) for char in line] for line in lines]
scrubberRating = [[int(char) for char in line] for line in lines]

for i in range(len(lines[0])):
    gamma = 1 if sum([1 if j == 1 else -1 for j in [rating[i] for rating in oxygenRating]]) >= 0 else 0
    epsilon = 1 if sum([1 if j == 1 else -1 for j in [rating[i] for rating in scrubberRating]]) < 0 else 0
    oxygenRating = [rating for rating in oxygenRating if rating[i] == gamma] if len(oxygenRating) > 1 else oxygenRating
    scrubberRating = [rating for rating in scrubberRating if rating[i] == epsilon] if len(scrubberRating) > 1 else scrubberRating

oxygenRating = int(''.join([str(rating) for rating in oxygenRating[0]]), 2)
scrubberRating = int(''.join([str(rating) for rating in scrubberRating[0]]), 2)
print(oxygenRating * scrubberRating)
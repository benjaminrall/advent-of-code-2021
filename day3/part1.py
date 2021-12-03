with open("input.txt", "r") as f:
    lines = [line.replace("\n", "") for line in f.readlines()]
gamma = [ 1 if sum([ 1 if j == 1 else -1 for j in [int(line[i]) for line in lines] ]) > 0 else 0 for i in range(len(lines[0])) ]
epsilon = [ 0 if n == 1 else 1 for n in gamma ]

gammaB2 = sum([ 2 ** i if gamma[-(1 + i)] == 1 else 0 for i in range(len(gamma))])
epsilonB2 = sum([ 2 ** i if epsilon[-(1 + i)] == 1 else 0 for i in range(len(epsilon))])
print(gammaB2 * epsilonB2)
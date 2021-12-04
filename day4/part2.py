from part1 import *

with open("input.txt", "r") as f:
    lines = [line.replace("\n", "").strip() for line in f.readlines()]

drawnNumbers = [int(num) for num in lines[0].split(",")]
boards = makeBoards(lines, True)

drawnNumbers.reverse()
winTerms = None
for number in drawnNumbers:
    for board in boards:
        markNumber(board, number, False)
        if not checkWin(board):
            markNumber(board, number)
            winTerms = (board, number)
            break
    if winTerms is not None:
        break

print(winTerms)
sum = 0
for row in winTerms[0]:
    for col in row:
        if not col[1]:
            sum += col[0]

print(sum)

print(sum * winTerms[1])
with open("input.txt", "r") as f:
    lines = [line.replace("\n", "").strip() for line in f.readlines()]

drawnNumbers = [int(num) for num in lines[0].split(",")]

boards = []
currentBoard = []
for line in lines[2:]:
    if line == "":
        boards.append(currentBoard)
        currentBoard = []
    else:
        currentBoard.append([[int(num), False] for num in line.split(" ") if num != ""])
boards.append(currentBoard)

def markNumber(board, number):
    for row in board:
        for col in row:
            if col[0] == number:
                col[1] = True

def checkWin(board):
    for row in board:
        winningRow = True
        for col in row:
            if not col[1]:
                winningRow = False
                break
        if winningRow:
            return True
    for i in range(5):
        winningCol = True
        for row in board:
            if not row[i][1]:
                winningCol = False
                break
        if winningCol:
            return True
    return False

winTerms = None
for number in drawnNumbers:
    for board in boards:
        markNumber(board, number)
        if (checkWin(board)):
            winTerms = (board, number)
            break
    if winTerms is not None:
        break

sum = 0
for row in winTerms[0]:
    for col in row:
        if not col[1]:
            sum += col[0]

print(sum * winTerms[1])
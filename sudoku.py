

def verifyRow(grid, row, num):
    condition = True
    for x in range(0, len(grid[row])):
        if grid[row][x] == num:
            condition = False
    return condition


def verifyCol(grid, col, num):
    condition = True
    for x in range(0, len(grid)):
        if grid[x][col] == num:
            condition = False
    return condition


def verifyUnderGrid(grid, row, col, num):
    condition = True
    underrow = row//3
    undercol = col//3
    for x in range(underrow*3, (underrow+1)*3):
        for y in range(undercol*3, (undercol+1)*3):
            if grid[x][y] == num:
                condition = False
    return condition


def verifyValid(grid, row, col, num):
    condition = verifyCol(grid, col, num) and verifyUnderGrid(
        grid, row, col, num) and verifyRow(grid, row, num)
    return (condition)


def showGrid(grid):
    col = 0
    print()
    row = 0
    while row < len(grid):
        col = 0
        while col < len(grid[row]):
            print(grid[row][col], end="  ")
            col += 1
        print()
        row += 1


def solve(grid):
    counter = 0
    for x in range(0, len(grid)):
        for y in range(0, len(grid[x])):
            if grid[x][y] == 0:
                for n in range(1, 10):
                    if verifyValid(grid, x, y, n):
                        grid[x][y] = n
                        solve(grid)
                        if verifyWin(grid) == False:
                            grid[x][y] = 0
                return

    if verifyWin(grid) == True and counter != 1:
        counter = 1
        showGrid(grid)


def verifyWin(grid):
    condition = True
    for x in range(0, len(grid)):
        for y in range(0, len(grid[x])):
            if grid[x][y] == 0:
                condition = False
    return condition


grid = [[0, 0, 3, 0, 0, 7, 0, 6, 0],
        [0, 0, 7, 8, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 1],
        [0, 0, 5, 4, 0, 8, 3, 7, 9],
        [0, 3, 0, 2, 7, 9, 6, 4, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 7, 6, 3, 9, 4, 0, 0, 0],
        [0, 0, 4, 0, 0, 5, 0, 8, 0]]
showGrid(grid)
solve(grid)

for x in range(0,len(Grid)):
    for y in range(0, len(Grid[x])):
        if Grid[x]


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

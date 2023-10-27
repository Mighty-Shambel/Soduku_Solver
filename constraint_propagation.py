import numpy as np

grid = [
    [9, 0, 0, 7, 0, 6, 0, 3, 1],
    [6, 0, 0, 4, 0, 0, 8, 2, 0],
    [2, 0, 7, 3, 0, 0, 0, 0, 9],
    [0, 0, 2, 0, 0, 1, 4, 0, 0],
    [7, 0, 0, 0, 6, 0, 2, 0, 0],
    [1, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 0, 0],
    [0, 6, 0, 0, 8, 9, 0, 7, 0],
    [4, 0, 9, 6, 0, 0, 0, 0, 0],
]

def possible(row, column, number):
    global grid

    # Check if the number appears in the row
    if number in grid[row]:
        return False

    # Check if the number appears in the column
    if number in [grid[i][column] for i in range(9)]:
        return False

    # Check if the number exists in the 3x3 matrix
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == number:
                return False
    return True

def solve():
    global grid

    for row in range(9):
        for column in range(9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0

                return

    # When the entire grid is filled, print the solution
    print(np.matrix(grid))
    input("There are more possible solutions")

# A Sudoku puzzle with constraint propagation
def sudoku_solver(grid):
    solve()

sudoku_solver(grid)

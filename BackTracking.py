import numpy as np

grid = [
    [4, 0, 9, 5, 0, 1, 6, 0, 0],
    [0, 5, 0, 0, 0, 9, 0, 3, 0],
    [3, 0, 6, 0, 0, 0, 0, 0, 0],
    [8, 0, 3, 9, 0, 2, 0, 0, 0],
    [0, 2, 4, 0, 0, 0, 0, 0, 0],
    [1, 6, 5, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 5, 0, 0, 8, 4],
    [0, 4, 0, 0, 1, 0, 3, 0, 0],
    [2, 0, 8, 4, 0, 0, 1, 0, 0],
]

def possible(row, column, number):
    global grid
    # Check if the number is valid in the row and column
    for i in range(9):
        if grid[row][i] == number or grid[i][column] == number:
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

                        # Apply constraint propagation by updating domains
                        if solve():
                            return True  # A solution was found
                        else:
                            grid[row][column] = 0  # Backtrack

                return False  # No valid number found; need to backtrack

    # All cells filled; a solution was found
    return True

if solve():
    print(np.matrix(grid))
else:
    print("No solution exists.")

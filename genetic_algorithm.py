import numpy as np
import random

# Your Sudoku grid
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


def is_complete():
    for row in grid:
        if 0 in row:
            return False
    return True


def fitness(candidate):
    fitness_score = 0
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                if possible(row, col, candidate[row][col]):
                    fitness_score += 1
    return fitness_score


def create_individual():
    individual = []
    for row in range(9):
        individual.append(random.sample(range(1, 10), 9))
    return individual


def crossover(parent1, parent2):
    child = []
    for i in range(9):
        if i % 2 == 0:
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    return child


def mutate(individual):
    for row in range(9):
        if random.random() < 0.1:
            individual[row] = random.sample(range(1, 10), 9)
    return individual


def genetic_algorithm(population_size, generations):
    population = [create_individual() for _ in range(population_size)]

    for generation in range(generations):
        population = sorted(population, key=fitness, reverse=True)
        if fitness(population[0]) == 81 or is_complete():
            return population[0]

        new_population = population[:population_size // 2]

        for _ in range(population_size // 2):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = mutate(crossover(parent1, parent2))
            new_population.append(child)

        population = new_population

    return population[0]


def solve_sudoku_with_genetic_algorithm():
    global grid
    solved_grid = genetic_algorithm(50, 100)
    for row in range(9):
        for col in range(9):
            grid[row][col] = solved_grid[row][col]
    if is_complete():
        print(np.matrix(grid))
    else:
        print("No solution found with the genetic algorithm.")


solve_sudoku_with_genetic_algorithm()

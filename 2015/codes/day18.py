import numpy as np
with open('../inputs/day18') as f:
    data = f.readlines()

def count_neighbors(grid, row, col):
    count = 0
    directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]

    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == '#':
            count += 1

    return count

def update_grid(grid):
    new_grid = [list(row) for row in grid]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            neighbors = count_neighbors(grid, i, j)

            if grid[i][j] == '#' and neighbors not in (2, 3):
                new_grid[i][j] = '.'
            elif grid[i][j] == '.' and neighbors == 3:
                new_grid[i][j] = '#'

    return new_grid

def animate_lights(initial_grid, steps):
    current_grid = initial_grid

    for _ in range(steps):
        current_grid = update_grid(current_grid)

    return sum(row.count('#') for row in current_grid)

result = animate_lights(data, 100)
print("Lights on after 100 steps:", result)

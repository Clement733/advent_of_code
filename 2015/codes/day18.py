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
            if (i == 0 or i == len(grid) - 1) and (j == 0 or j == len(grid[0]) - 1):
                # Skip the corner cells
                continue

            neighbors = count_neighbors(grid, i, j)

            if grid[i][j] == '#' and neighbors not in (2, 3):
                new_grid[i][j] = '.'
            elif grid[i][j] == '.' and neighbors == 3:
                new_grid[i][j] = '#'

    # Set the four corners to always be on
    new_grid[0][0] = '#'
    new_grid[0][-1] = '#'
    new_grid[-1][0] = '#'
    new_grid[-1][-1] = '#'

    return new_grid

def animate_lights(initial_grid, steps):
    current_grid = initial_grid

    for _ in range(steps):
        current_grid = update_grid(current_grid)

    return sum(row.count('#') for row in current_grid)

corners = { (0,0), (0,99), (99,0), (99,99) }
with open('../inputs/day18') as f:
    lights = corners | {(x,y) for y, line in enumerate(f)
                        for x, char in enumerate(line.strip())
                        if char == '#'}

neighbours = lambda x,y: sum((_x,_y) in lights for _x in (x-1,x,x+1)
                            for _y in (y-1,y,y+1) if (_x, _y) != (x, y))

for c in range(100):
    lights = corners | {(x,y) for x in range(100) for y in range(100)
                        if (x,y) in lights and 2 <= neighbours(x,y) <= 3
                        or (x,y) not in lights and neighbours(x,y) == 3}
print (len(lights))

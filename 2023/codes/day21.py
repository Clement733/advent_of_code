# with open('../inputs/day21') as f:
#     lines = f.readlines()

# for x, row in enumerate(lines):
#     for y, col in enumerate(row):
#         if "S" in row:
#             start = [x, y]

# print(start)
# grid_x = len(lines[0])
# grid_y = len(lines)-1
# print(grid_x)
# print(grid_y)
# grid = [list(row.strip()) for row in lines]
# print(grid)
def count_paths(x, y, steps, grid, memo):
    if steps == 0:
        return 1  # Reached the target number of steps

    if (x, y, steps) in memo:
        return memo[(x, y, steps)]

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    count = 0

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy

        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == '.':
            count += count_paths(new_x, new_y, steps - 1, grid, memo)

    memo[(x, y, steps)] = count
    return count

if __name__ == "__main__":
    with open('../inputs/day21') as f:
        lines = f.readlines()

    grid = [list(row.strip()) for row in lines]

    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if col == "S":
                start = (x, y)

    if start is not None:
        max_steps = 64
        result = count_paths(start[0], start[1], max_steps, grid, {})
        print("Number of garden plots reachable in exactly 64 steps:", result)
    else:
        print("Starting position not found.")

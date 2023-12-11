from itertools import combinations
import numpy as np

def man(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def find_paths(data, expand=100000):
    matrix = np.array([list(line.strip()) for line in data])

    empty_rows = np.all(matrix == '.', axis=1)
    empty_cols = np.all(matrix == '.', axis=0)

    real_matrix = np.insert(matrix, np.where(empty_cols)[0], '.', axis=1)
    real_matrix = np.insert(real_matrix, np.where(empty_rows)[0], '.', axis=0)

    coords = np.argwhere(real_matrix == '#')
    indicies = {tuple(coord): i+1 for i, coord in enumerate(coords)}

    for coord in coords:
        coord[0] += np.sum(coord[0] > empty_rows) * (expand - 1)
        coord[1] += np.sum(coord[1] > empty_cols) * (expand - 1)

    total_path_length = sum(man(coords[i], coords[j])
                            for i, j in combinations(range(len(coords)), 2))

    return total_path_length

with open('../inputs/day11') as f:
    data = f.read().split()

print(find_paths(data, 1))
print(find_paths(data, 100000))
from itertools import accumulate

g = [(x,y) for y,r in enumerate(data)
           for x,c in enumerate(r) if c == '#']

def dist(ps):
    *exp, = accumulate((l, 1)[p in ps] for p in range(max(ps)+1))
    return sum(abs(exp[a]-exp[b]) for a,b in combinations(ps, 2))

for l in 2, 1_000_000: print(sum(map(dist, zip(*g))))
